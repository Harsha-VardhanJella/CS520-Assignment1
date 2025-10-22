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
    tol = 1e-6

    # Find initial interval [a, b] where poly(xs, a) and poly(xs, b) have different signs
    a, b = -1, 1
    fa, fb = poly(xs, a), poly(xs, b)
    for _ in range(max_iter):
        if fa * fb < 0:
            break
        if abs(fa) < abs(fb):
            a -= (b - a) * 1.5
            fa = poly(xs, a)
        else:
            b += (b - a) * 1.5
            fb = poly(xs, b)
    else:
        raise ValueError("Failed to find root")

    # Refine the root using bisection method
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