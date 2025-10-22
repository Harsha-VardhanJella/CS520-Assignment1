import math

def poly(xs: list, x: float):
    return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

def find_zero(xs: list):
    def derivative(xs):
        return [i * xs[i] for i in range(1, len(xs))]

    d_xs = derivative(xs)
    x = 0.0
    for _ in range(10000):
        fx = poly(xs, x)
        dfx = poly(d_xs, x)
        if abs(fx) < 1e-10:
            return x
        if dfx == 0:
            x += 1e-3
            continue
        x_new = x - fx / dfx
        if abs(x_new - x) < 1e-10:
            return x_new
        x = x_new
    return x
