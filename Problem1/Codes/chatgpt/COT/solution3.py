# def poly_deriv(xs, x):
#     return sum(i * xs[i] * math.pow(x, i - 1) for i in range(1, len(xs)))

# # quick checks
# if not xs:
#     raise ValueError("No coefficients")
# # constant polynomial
# if len(xs) == 1:
#     if abs(xs[0]) < tol:
#         return 0.0
#     raise ValueError("Polynomial is constant non-zero; no real root")
# # check zero
# try:
#     if abs(poly(xs, 0.0)) < tol:
#         return 0.0
# except Exception:
#     # if poly not defined in environment, define local Horner
#     def _poly(xs, x):
#         res = 0.0
#         for a in reversed(xs):
#             res = res * x + a
#         return res
#     if abs(_poly(xs, 0.0)) < tol:
#         return 0.0

# # sampling strategy to find sign changes or near-zero points
# def sample_and_find():
#     best_x = None
#     best_val = float("inf")
#     # try widening scales
#     for exp in range(0, 7):
#         scale = 1.5 ** exp
#         # 101 samples from -scale to +scale
#         n = 101
#         xsamples = [(-scale + 2 * scale * i / (n - 1)) for i in range(n)]
#         prev_x = xsamples[0]
#         prev_val = poly(xs, prev_x)
#         if abs(prev_val) < best_val:
#             best_val = abs(prev_val); best_x = prev_x
#         for x in xsamples[1:]:
#             val = poly(xs, x)
#             if abs(val) < best_val:
#                 best_val = abs(val); best_x = x
#             # sign change -> bracket found
#             if prev_val == 0.0:
#                 return prev_x, prev_x
#             if val == 0.0:
#                 return x, x
#             if prev_val * val < 0.0:
#                 return prev_x, x
#             prev_x, prev_val = x, val
#     return None, best_x

# bracket, near_x = sample_and_find()
# # if bracket found, do bisection
# if bracket is not None:
#     a, b = bracket
#     fa = poly(xs, a)
#     fb = poly(xs, b)
#     if a == b:
#         return float(a)
#     # ensure signs
#     if fa * fb > 0:
#         # rare: if same sign despite detection, fallback to near_x
#         if near_x is not None:
#             return float(near_x)
#     for _ in range(max_bisect_iters):
#         m = 0.5 * (a + b)
#         fm = poly(xs, m)
#         if abs(fm) < 1e-14:
#             return float(m)
#         if fa * fm < 0:
#             b, fb = m, fm
#         else:
#             a, fa = m, fm
#         if abs(b - a) < tol:
#             return float(0.5 * (a + b))
#     return float(0.5 * (a + b))

# # No sign change found. If near sample is very close, return it
# if near_x is not None and abs(poly(xs, near_x)) < 1e-8:
#     return float(near_x)

# # Try Newton-Raphson from several starting points (samples)
# # prepare starting points: small grid
# starts = []
# for r in [0.0, 1.0, -1.0, 2.0, -2.0]:
#     starts.append(r)
# for k in range(1, 9):
#     starts.append(0.5 * k)
#     starts.append(-0.5 * k)
# # unique starts
# seen = set()
# starts = [x for x in starts if not (x in seen or seen.add(x))]
# for x0 in starts:
#     x = float(x0)
#     for _ in range(max_newton_iters):
#         fx = poly(xs, x)
#         if abs(fx) < 1e-14:
#             return float(x)
#         dfx = poly_deriv(xs, x)
#         if dfx == 0:
#             break
#         dx = fx / dfx
#         # damping
#         if abs(dx) > 1.0:
#             dx = math.copysign(1.0, dx)
#         x_new = x - dx
#         if math.isinf(x_new) or math.isnan(x_new):
#             break
#         if abs(x_new - x) < tol:
#             if abs(poly(xs, x_new)) < 1e-10:
#                 return float(x_new)
#             break
#         x = x_new
#     # try tiny adjustments around x0
#     for shift in (1e-3, -1e-3, 1e-2, -1e-2):
#         try_x = x0 + shift
#         for _ in range(50):
#             fx = poly(xs, try_x)
#             if abs(fx) < 1e-14:
#                 return float(try_x)
#             dfx = poly_deriv(xs, try_x)
#             if dfx == 0:
#                 break
#             try_x_new = try_x - fx / dfx
#             if abs(try_x_new - try_x) < tol:
#                 if abs(poly(xs, try_x_new)) < 1e-10:
#                     return float(try_x_new)
#                 break
#             try_x = try_x_new

# # last resort: search large range for sign change at exponentially growing bounds
# prev_x = -1.0
# prev_val = poly(xs, prev_x)
# if abs(prev_val) < 1e-14:
#     return float(prev_x)
# for k in range(0, 60):
#     x = (2.0 ** k)
#     for x_candidate in (x, -x):
#         val = poly(xs, x_candidate)
#         if abs(val) < 1e-14:
#             return float(x_candidate)
#         if prev_val * val < 0:
#             # bracket found between prev_x and x_candidate
#             a, b = prev_x, x_candidate
#             fa, fb = prev_val, val
#             for _ in range(max_bisect_iters):
#                 m = 0.5 * (a + b)
#                 fm = poly(xs, m)
#                 if abs(fm) < 1e-14:
#                     return float(m)
#                 if fa * fm < 0:
#                     b, fb = m, fm
#                 else:
#                     a, fa = m, fm
#                 if abs(b - a) < tol:
#                     return float(0.5 * (a + b))
#             return float(0.5 * (a + b))
#         prev_x, prev_val = x_candidate, val

# # if nothing found, return the point with the smallest absolute value encountered
# # search a fine grid and pick minimum
# best_x = None
# best_val = float("inf")
# for scale in (1.0, 10.0, 100.0, 1000.0):
#     n = 201
#     for i in range(n):
#         x = -scale + 2 * scale * i / (n - 1)
#         val = abs(poly(xs, x))
#         if val < best_val:
#             best_val = val; best_x = x
#             if val < 1e-10:
#                 return float(x)
# if best_x is None:
#     return 0.0
# return float(best_x)
