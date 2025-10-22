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
    # Define the tolerance and maximum interval size
    tol = 1e-12
    max_size = 1e6
    
    # Evaluate the polynomial at x = 0
    y = poly(xs, 0)
    
    # Determine the initial interval
    if y == 0:
        return 0
    
    # Bracket the sign change
    a, b = 0, 1
    ya, yb = y, poly(xs, b)
    
    # Expand the interval until a sign change is detected
    while ya * yb > 0:
        if abs(ya) < abs(yb):
            a -= (b - a)
            ya = poly(xs, a)
        else:
            b += (b - a)
            yb = poly(xs, b)
        
        # Check if the interval has exceeded the maximum size
        if abs(b - a) > max_size:
            raise ValueError("Failed to bracket the root")
    
    # Apply bisection to find the root
    while abs(b - a) > tol:
        c = (a + b) / 2
        yc = poly(xs, c)
        
        if yc == 0:
            return c
        elif ya * yc < 0:
            b, yb = c, yc
        else:
            a, ya = c, yc
    
    return (a + b) / 2