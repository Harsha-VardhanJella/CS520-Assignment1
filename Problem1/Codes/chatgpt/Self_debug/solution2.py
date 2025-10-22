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
    Uses a robust method: expand interval to bracket root, then bisection.
    """
    # Initial guess interval
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)
    
    # Expand interval until a sign change is found
    step = 1.0
    max_expand = 1e6
    while fa * fb > 0 and step < max_expand:
        a -= step
        b += step
        fa, fb = poly(xs, a), poly(xs, b)
        step *= 2
    
    if fa * fb > 0:
        raise ValueError("Failed to bracket a root.")
    
    # Bisection method
    tol = 1e-12
    while abs(b - a) > tol:
        c = (a + b) / 2
        fc = poly(xs, c)
        if abs(fc) < tol:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2
