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
    # Define the tolerance and maximum interval size
    tol = 1e-12
    max_size = 1e6

    # Check if the polynomial is a constant
    if len(xs) == 1:
        if xs[0] == 0:
            return 0.0
        else:
            return None

    # Find the initial interval [a, b] such that poly(xs, a) and poly(xs, b) have different signs
    a = -1.0
    b = 1.0
    fa = poly(xs, a)
    fb = poly(xs, b)

    # Expand the interval until we bracket a sign change
    while fa * fb > 0:
        if abs(fa) < abs(fb):
            a -= (b - a) * 1.5
            fa = poly(xs, a)
        else:
            b += (b - a) * 1.5
            fb = poly(xs, b)

        # Check if the interval has grown too large
        if abs(b - a) > max_size:
            return None

    # Apply bisection to find the root
    while abs(b - a) > tol:
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

    return (a + b) / 2