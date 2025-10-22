import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Example: if xs = [a0, a1, a2], returns a0 + a1*x + a2*x**2
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """
    Return one real x such that poly(xs, x) ≈ 0 using a bracketing and bisection approach.
    """
    tol = 1e-12
    max_iter = 1000
    a, b = -1.0, 1.0

    # Expand interval until a sign change is found
    for _ in range(max_iter):
        fa, fb = poly(xs, a), poly(xs, b)
        if math.isnan(fa) or math.isnan(fb):
            a, b = -1.0, 1.0
        if fa * fb <= 0:
            break
        a *= 2
        b *= 2
    else:
        # fallback in case no sign change found
        return 0.0

    # Bisection method
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = poly(xs, c)
        if abs(fc) < tol:
            return c
        if poly(xs, a) * fc < 0:
            b = c
        else:
            a = c
    return (a + b) / 2
