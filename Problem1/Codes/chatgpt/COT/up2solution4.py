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

    if fa == 0:
        return a
    if fb == 0:
        return b

    # Expand interval until sign change or 200 expansions
    for _ in range(200):
        if not (math.isfinite(fa) and math.isfinite(fb)):
            return a
        if fa * fb < 0:
            break
        a *= 2
        b *= 2
        fa, fb = poly(xs, a), poly(xs, b)
    else:
        return a  # No sign change found

    # Bisection method
    for _ in range(200):
        mid = (a + b) / 2
        fm = poly(xs, mid)
        if not math.isfinite(fm):
            break
        if abs(b - a) < 1e-10:
            break
        if fm == 0:
            return mid
        if fa * fm < 0:
            b, fb = mid, fm
        else:
            a, fa = mid, fm

    return a
