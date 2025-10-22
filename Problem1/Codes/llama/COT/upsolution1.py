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
    Use a robust numerical method: bracket a sign change by expanding an initial interval,
    then apply bisection until the interval is sufficiently small.
    """
    # Initial interval
    a = -1.0
    b = 1.0
    
    # Evaluate the polynomial at the interval endpoints
    fa = poly(xs, a)
    fb = poly(xs, b)
    
    # Expand the interval until we bracket a root
    while fa * fb > 0:
        if abs(fa) < abs(fb):
            a -= 1.6 * (b - a)
            fa = poly(xs, a)
        else:
            b += 1.6 * (b - a)
            fb = poly(xs, b)
    
    # Apply bisection until the interval is sufficiently small
    while b - a > 1e-6:
        c = (a + b) / 2
        fc = poly(xs, c)
        if fc == 0:
            return c
        elif fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    
    # Return the midpoint of the final interval
    return (a + b) / 2