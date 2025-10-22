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
    Uses interval expansion to bracket a root and bisection for refinement.
    """
    # Initial guess
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)
    
    # Expand interval until a sign change is found
    step = 1.0
    max_expand = 1e6
    while fa * fb > 0 and (abs(a) < max_expand and abs(b) < max_expand):
        a -= step
        b += step
        fa, fb = poly(xs, a), poly(xs, b)
        step *= 1.5  # gradually increase expansion
    
    # If still no sign change, fallback to scanning
    if fa * fb > 0:
        for i in range(-1000, 1001):
            x = i * 0.1
            if poly(xs, x) == 0:
                return x
            if i != -1000:
                prev_x = (i-1) * 0.1
                if poly(xs, prev_x) * poly(xs, x) < 0:
                    a, b = prev_x, x
                    break
    
    # Bisection method
    tol = 1e-12
    max_iter = 1000
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = poly(xs, c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2
