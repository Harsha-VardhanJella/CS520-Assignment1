# import math

# def poly(xs: list, x: float):
#     """
#     Evaluates polynomial with coefficients xs at point x.
#     Example: if xs = [a0, a1, a2], returns a0 + a1*x + a2*x**2
#     """
#     return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

# def find_zero(xs: list):
#     """
#     Return one real x such that poly(xs, x) ≈ 0.
#     Use a robust numerical method: bracket a sign change by expanding an initial interval,
#     then apply bisection until the interval is sufficiently small.
#     """
#     # Initial guess for the interval
#     a = -1.0
#     b = 1.0

#     # Bracket a sign change
#     while math.copysign(1, poly(xs, a)) == math.copysign(1, poly(xs, b)):
#         if abs(poly(xs, a)) < abs(poly(xs, b)):
#             b = a
#             a *= 2
#         else:
#             a = b
#             b *= 2

#     # Apply bisection
#     tol = 1e-12
#     while abs(b - a) > tol:
#         c = (a + b) / 2
#         if math.copysign(1, poly(xs, a)) == math.copysign(1, poly(xs, c)):
#             a = c
#         else:
#             b = c

#     return (a + b) / 2

# # Test cases
# print(find_zero([1, 2]))
# print(find_zero([-6, 11, -6, 1]))