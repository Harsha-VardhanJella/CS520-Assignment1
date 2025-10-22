import math

def poly(xs, x):
    """
    Evaluates polynomial with coefficients xs at point x.
    Example: if xs = [a0, a1, a2], returns a0 + a1*x + a2*x**2
    """
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs):
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
    """
    a = -1.0
    b = 1.0

    # Evaluate endpoints
    pa = poly(xs, a)
    if pa == 0:
        return a
    pb = poly(xs, b)
    if pb == 0:
        return b

    # Expand interval symmetrically until sign change or 200 expansions
    expansion = 0
    while expansion < 200 and math.copysign(1, pa) == math.copysign(1, pb):
        a *= 2
        b *= 2
        pa_new = poly(xs, a)
        pb_new = poly(xs, b)
        if not (math.isfinite(pa_new) and math.isfinite(pb_new)):
            break
        pa, pb = pa_new, pb_new
        expansion += 1

    # Apply bisection until (b - a) < 1e-10 or 200 iterations
    iteration = 0
    while iteration < 200 and b - a >= 1e-10:
        c = (a + b) / 2
        pc = poly(xs, c)
        if pc == 0:
            return c
        elif math.copysign(1, pa) != math.copysign(1, pc):
            b = c
            pb = pc
        else:
            a = c
            pa = pc
        iteration += 1

    # Return left bound of final interval
    return a