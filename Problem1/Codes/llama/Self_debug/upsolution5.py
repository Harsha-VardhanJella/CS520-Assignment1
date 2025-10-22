import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Example: if xs = [a0, a1, a2], returns a0 + a1*x + a2*x**2
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """
    Return one real x such that poly(xs, x) ≈ 0.
    """
    max_iter = 1000
    tol = 1e-12
    
    # Initialize interval
    a, b = -1.0, 1.0
    
    # Check if we already have a bracket
    fa, fb = poly(xs, a), poly(xs, b)
    if fa * fb > 0:
        # Expand interval until we bracket a root
        iter_count = 0
        while fa * fb > 0 and iter_count < max_iter:
            if abs(fa) < abs(fb):
                a -= (b - a)
                fa = poly(xs, a)
            else:
                b += (b - a)
                fb = poly(xs, b)
            iter_count += 1
        if fa * fb > 0:  # Failed to bracket
            raise ValueError("Failed to find a root")
    
    # Refine the bracket using bisection
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = poly(xs, c)
        if abs(fc) < tol or (b - a) / 2 < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    raise ValueError("Failed to converge")