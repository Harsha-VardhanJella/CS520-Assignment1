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
    Use a robust numerical method: bracket a sign change by expanding an initial interval,
    then apply bisection until the interval is sufficiently small.
    """
    # Define the initial interval and expansion factor
    left, right = -1.0, 1.0
    expansion_factor = 1.5
    
    # Bracket the root
    while poly(xs, left) * poly(xs, right) > 0:
        if abs(poly(xs, left)) < abs(poly(xs, right)):
            left = left * expansion_factor
        else:
            right = right * expansion_factor
    
    # Apply bisection
    tolerance = 1e-10
    max_iterations = 1000
    for _ in range(max_iterations):
        midpoint = (left + right) / 2
        if abs(poly(xs, midpoint)) < tolerance or abs(right - left) < tolerance:
            return midpoint
        if poly(xs, left) * poly(xs, midpoint) < 0:
            right = midpoint
        else:
            left = midpoint
    
    # If max iterations reached without finding a root, return the current estimate
    return (left + right) / 2