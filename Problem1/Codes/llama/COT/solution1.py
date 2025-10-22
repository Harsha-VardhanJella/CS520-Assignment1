import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Example: if xs = [a0, a1, a2], returns a0 + a1*x + a1*x**2
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """Return one real x such that poly(xs, x) ≈ 0."""
    def derivative(x):
        return sum(i * coeff * math.pow(x, i-1) for i, coeff in enumerate(xs) if i > 0)

    x = 0.0
    learning_rate = 0.1
    precision = 0.000001
    max_iterations = 1000
    iteration = 0

    while iteration < max_iterations:
        fx = poly(xs, x)
        if abs(fx) < precision:
            return x
        dfx = derivative(x)
        if dfx == 0:
            break
        x = x - fx / dfx
        iteration += 1
    return x