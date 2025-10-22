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
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)

    # Check endpoints
    if fa == 0:
        return a
    if fb == 0:
        return b

    # Expand interval
    for _ in range(200):
        if not (math.isfinite(fa) and math.isfinite(fb)):
            return float('nan')
        if fa * fb < 0:
            break
        a *= 2
        b *= 2
        fa, fb = poly(xs, a), poly(xs, b)
    else:
        return float('nan')

    # Bisection method
    for _ in range(200):
        if (b - a) < 1e-10:
            break
        mid = 0.5 * (a + b)
        fm = poly(xs, mid)
        if not math.isfinite(fm):
            return float('nan')
        if fm == 0:
            return mid
        if fa * fm < 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm

    return a
