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
    # Define the initial interval and the maximum interval size
    left, right = -1.0, 1.0
    max_interval_size = 1e6
    
    # Bracket a sign change by expanding the interval
    while (poly(xs, left) * poly(xs, right) > 0 and 
           abs(right - left) < max_interval_size):
        if abs(poly(xs, left)) < abs(poly(xs, right)):
            left *= 2
        else:
            right *= 2
    
    # Check if we exceeded the maximum interval size
    if abs(right - left) >= max_interval_size:
        raise ValueError("No root found within the maximum interval size")
    
    # Apply bisection until the interval is sufficiently small
    tolerance = 1e-10
    while abs(right - left) > tolerance:
        midpoint = (left + right) / 2
        if poly(xs, midpoint) * poly(xs, left) <= 0:
            right = midpoint
        else:
            left = midpoint
    
    # Return the midpoint of the final interval
    return (left + right) / 2