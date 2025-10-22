# import math

# def poly(xs: list, x: float):
# return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

# def find_zero(xs: list):
# def sign(v): return 1 if v > 0 else -1 if v < 0 else 0
# a, b = -1.0, 1.0
# fa, fb = poly(xs, a), poly(xs, b)
# # Expand interval until sign change
# while sign(fa) == sign(fb):
# a *= 2
# b *= 2
# fa, fb = poly(xs, a), poly(xs, b)
# if abs(a) > 1e6: break
# # Bisection method
# for _ in range(100):
# m = 0.5 * (a + b)
# fm = poly(xs, m)
# if abs(fm) < 1e-12:
# return m
# if sign(fa) != sign(fm):
# b, fb = m, fm
# else:
# a, fa = m, fm
# return m
