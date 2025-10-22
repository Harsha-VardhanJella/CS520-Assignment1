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
    max_iter = 1000
    tol = 1e-12

    # Expand interval until sign change is found
    for _ in range(max_iter):
        fa, fb = poly(xs, a), poly(xs, b)
        if math.isnan(fa) or math.isnan(fb):
            a, b = a*2, b*2
            continue
        if fa * fb <= 0:
            break
        a, b = a*2, b*2
    else:
        raise ValueError("Failed to bracket a root.")

    # Bisection method
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = poly(xs, c)
        if abs(fc) < tol or abs(b - a) < tol:
            return c
        if fc * poly(xs, a) <= 0:
            b = c
        else:
            a = c

    return (a + b) / 2
