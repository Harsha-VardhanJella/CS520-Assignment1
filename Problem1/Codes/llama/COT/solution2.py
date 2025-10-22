import math

def poly(xs: list, x: float):
    """
    Evaluates polynomial with coefficients xs at point x.
    Example: if xs = [a0, a1, a2], returns a0 + a1*x + a2*x**2
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    """Return one real x such that poly(xs, x) ≈ 0."""
    def derivative(xs, x, epsilon=1e-7):
        return (poly(xs, x + epsilon) - poly(xs, x - epsilon)) / (2 * epsilon)

    x = 0.0
    learning_rate = 0.1
    precision = 1e-5
    max_iterations = 1000

    for _ in range(max_iterations):
        x_next = x - learning_rate * poly(xs, x) / derivative(xs, x)
        if abs(x_next - x) < precision:
            return x_next
        x = x_next
    return x