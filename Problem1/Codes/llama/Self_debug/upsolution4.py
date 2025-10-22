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
    def evaluate(x):
        return poly(xs, x)

    a, b = -1, 1
    fa, fb = evaluate(a), evaluate(b)
    max_iter = 1000

    # Check if endpoints are roots or expand interval
    iter_count = 0
    while fa * fb > 0 and iter_count < max_iter:
        if abs(fa) < abs(fb):
            a -= (b - a) * 0.5
            fa = evaluate(a)
        else:
            b += (b - a) * 0.5
            fb = evaluate(b)
        iter_count += 1

    if fa * fb > 0:
        raise ValueError("Failed to find root")

    # Refine root using bisection method
    while abs(b - a) > 1e-6 and iter_count < max_iter:
        c = (a + b) / 2
        fc = evaluate(c)
        if fc == 0:
            return c
        elif fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
        iter_count += 1

    return (a + b) / 2