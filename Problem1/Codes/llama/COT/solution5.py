import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Example: if xs = [a0, a1, a2], returns a0 + a1*x + a2*x**2
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """Return one real x such that poly(xs, x) ≈ 0."""
    def f(x):
        return poly(xs, x)

    def df(x, epsilon=1e-8):
        return (f(x + epsilon) - f(x)) / epsilon

    x = 0.0
    for _ in range(100):
        x_next = x - f(x) / df(x)
        if abs(x_next - x) < 1e-6:
            return x_next
        x = x_next
    return x