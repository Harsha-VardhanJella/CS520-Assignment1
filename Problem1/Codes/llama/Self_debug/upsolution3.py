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
        result = poly(xs, x)
        if not math.isfinite(result):
            return float('inf') if result > 0 else -float('inf')
        return result

    a, b = -1, 1
    fa, fb = evaluate(a), evaluate(b)
    max_iter = 100

    # Expand interval until we bracket a root
    for _ in range(max_iter):
        if fa * fb < 0:
            break
        if abs(fa) < abs(fb):
            a -= (b - a) * 1.5
            fa = evaluate(a)
        else:
            b += (b - a) * 1.5
            fb = evaluate(b)

    # Refine the root using bisection method
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = evaluate(c)
        if abs(fc) < 1e-6 or abs(b - a) < 1e-6:
            return c
        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    # If max iterations reached, return the best estimate
    return a if abs(fa) < abs(evaluate(b)) else b