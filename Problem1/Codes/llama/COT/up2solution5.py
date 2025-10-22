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
    Requirements:
    - Start with a = -1.0 and b = 1.0
    - If poly(xs, a) == 0 or poly(xs, b) == 0, return that endpoint
    - Expand the interval symmetrically (a *= 2, b *= 2) until a sign change occurs
    or 200 expansions have been attempted
    - Abort expansion if values become non-finite
    - Once a sign change is found, apply bisection until (b - a) < 1e-10 or 200 iterations
    - Return the left bound of the final interval
    - Do not print anything or import any libraries other than math
    """
    a = -1.0
    b = 1.0
    
    # Check if endpoints are zeros
    if poly(xs, a) == 0:
        return a
    if poly(xs, b) == 0:
        return b

    # Expand interval symmetrically until sign change or 200 attempts
    for _ in range(200):
        fa = poly(xs, a)
        fb = poly(xs, b)
        
        if not (math.isfinite(fa) and math.isfinite(fb)):
            break
        
        if fa * fb < 0:
            break
        
        a *= 2
        b *= 2

    # Apply bisection
    for _ in range(200):
        c = (a + b) / 2
        fc = poly(xs, c)
        
        if not math.isfinite(fc):
            break
        
        if fc == 0:
            return c
        
        if fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
        
        if b - a < 1e-10:
            break

    return a