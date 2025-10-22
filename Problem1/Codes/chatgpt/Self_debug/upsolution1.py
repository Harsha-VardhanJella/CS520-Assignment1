import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Example: if xs = [a0, a1, a2], returns a0 + a1*x + a2*x**2
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """
    Return one real x such that poly(xs, x) ≈ 0 using bisection method.
    """
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)
    # Expand interval until a sign change is found
    for _ in range(50):
        if fa * fb <= 0:
            break
        a, b = a*2, b*2
        fa, fb = poly(xs, a), poly(xs, b)
    else:
        # fallback to 0 if no root found in expanded interval
        return 0.0
    # Bisection refinement
    for _ in range(100):
        c = (a + b) / 2
        fc = poly(xs, c)
        if abs(fc) < 1e-12 or (b - a)/2 < 1e-12:
            return c
        if fa * fc <= 0:
            b, fb = c, fc
        else:
            a, fa = c, fc
    return (a + b) / 2
