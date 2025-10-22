import math

def poly(xs: list, x: float):
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    def deriv(xs):
        return [i * xs[i] for i in range(1, len(xs))]

    d = deriv(xs)
    x = 0.0
    for _ in range(1000):
        fx = poly(xs, x)
        dfx = poly(d, x)
        if abs(dfx) < 1e-12:
            x += 1.0
            continue
        x_new = x - fx / dfx
        if abs(x_new - x) < 1e-10:
            return x_new
        x = x_new
    return x
