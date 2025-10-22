import math

def poly(xs: list, x: float):
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    # Initial guess
    a, b = -1.0, 1.0
    fa, fb = poly(xs, a), poly(xs, b)
    
    # Expand interval until a sign change is found
    step = 1.0
    while fa * fb > 0:
        a -= step
        b += step
        fa, fb = poly(xs, a), poly(xs, b)
        step *= 2
    
    # Bisection method
    tol = 1e-12
    max_iter = 1000
    for _ in range(max_iter):
        c = (a + b) / 2
        fc = poly(xs, c)
        if abs(fc) < tol or (b - a)/2 < tol:
            return c
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (a + b) / 2
