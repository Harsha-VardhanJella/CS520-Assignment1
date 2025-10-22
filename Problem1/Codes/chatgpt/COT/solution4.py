# Thought for 18s

# import math

# def poly(xs: list, x: float):
# """
# Evaluates polynomial with coefficients xs at point x.
# Example: if xs = [a0, a1, a2], returns a0 + a1x + a2x**2
# """
# return sum(coeff * math.pow(x, i) for i, coeff in enumerate(xs))

# def _sign(x):
# if x > 0: return 1
# if x < 0: return -1
# return 0

# def _bisection(xs, a, b, fa, fb, tol=1e-12, maxiter=200):
# if fa == 0.0:
# return float(a)
# if fb == 0.0:
# return float(b)
# lo, hi = a, b
# flo, fhi = fa, fb
# for _ in range(maxiter):
# mid = (lo + hi) / 2.0
# fmid = poly(xs, mid)
# if fmid == 0.0:
# return float(mid)
# # stop when interval is sufficiently small relative to scale
# if abs(hi - lo) <= tol * max(1.0, abs(lo), abs(hi), abs(mid)):
# return float(mid)
# if _sign(fmid) == _sign(flo):
# lo, flo = mid, fmid
# else:
# hi, fhi = mid, fmid
# return float((lo + hi) / 2.0)

# def find_zero(xs: list):
# """Return one real x such that poly(xs, x) ≈ 0."""
# # handle trivial cases
# if not xs:
# return 0.0
# # trim trailing zeros of highest degree if any (remove high-degree zero coefficients)
# # ensure representation is not all zeros
# last_nonzero = None
# for i in range(len(xs)-1, -1, -1):
# if xs[i] != 0:
# last_nonzero = i
# break
# if last_nonzero is None:
# # zero polynomial -> every x is a root; return 0
# return 0.0
# xs = xs[: last_nonzero + 1 ]
# # constant non-zero polynomial -> no real root
# if len(xs) == 1:
# raise ValueError("Polynomial is constant non-zero; no real root.")
# # fast check at 0
# f0 = poly(xs, 0.0)
# if f0 == 0.0:
# return 0.0
# # sample sequence: 0, 1, -1, 2, -2, 4, -4, 8, -8, ...
# prev_x = 0.0
# prev_f = f0
# max_val = 1e6
# val = 1.0
# for k in range(0, 80):
# if val > max_val:
# val = max_val
# for x in (val, -val):
# fx = poly(xs, x)
# if fx == 0.0:
# return float(x)
# if _sign(fx) != 0 and _sign(prev_f) != 0 and _sign(fx) != _sign(prev_f):
# # bracket found between prev_x and x (order might be prev_x < x or >)
# a, b = (prev_x, x) if prev_x < x else (x, prev_x)
# fa, fb = poly(xs, a), poly(xs, b)
# return _bisection(xs, a, b, fa, fb)
# # also check sign change between consecutive sampled magnitudes (prev magnitude and current magnitude)
# if _sign(fx) != 0 and _sign(prev_f) == 0:
# return float(prev_x)
# prev_x, prev_f = x, fx
# # increase magnitude
# val *= 2.0
# # If no bracket found, try a few targeted initial guesses and apply safeguarded Newton (damped)
# # build derivative coefficients
# deriv = [i * c for i, c in enumerate(xs)][1:]
# def poly_deriv(x):
# return sum(coeff * math.pow(x, i) for i, coeff in enumerate(deriv))
# guesses = [0.0, 1.0, -1.0, 2.0, -2.0, 10.0, -10.0, 100.0, -100.0]
# for g in guesses:
# x = float(g)
# for _ in range(200):
# fx = poly(xs, x)
# if abs(fx) <= 1e-14:
# return float(x)
# dfx = poly_deriv(x)
# if dfx == 0.0 or not math.isfinite(dfx):
# break
# dx = fx / dfx
# # damp step
# step = dx
# # limit step size to prevent divergence
# max_step = max(1.0, abs(x)) * 0.5
# if abs(step) > max_step:
# step = math.copysign(max_step, step)
# x_new = x - step
# if not math.isfinite(x_new):
# break
# # if no improvement in function value, reduce step
# if abs(poly(xs, x_new)) >= abs(fx):
# step *= 0.5
# x_new = x - step
# x = x_new
# # try small bracket around last x
# a, b = x - 1.0, x + 1.0
# fa, fb = poly(xs, a), poly(xs, b)
# if _sign(fa) != 0 and _sign(fb) != 0 and _sign(fa) != _sign(fb):
# return _bisection(xs, a, b, fa, fb)
# # As a final fallback, try scanning a dense grid in [-1000,1000]
# lo, hi = -1000.0, 1000.0
# steps = 2000
# prev_x = lo
# prev_f = poly(xs, prev_x)
# for i in range(1, steps + 1):
# x = lo + (hi - lo) * i / steps
# fx = poly(xs, x)
# if fx == 0.0:
# return float(x)
# if _sign(fx) != 0 and _sign(prev_f) != 0 and _sign(fx) != _sign(prev_f):
# a, b = (prev_x, x) if prev_x < x else (x, prev_x)
# fa, fb = poly(xs, a), poly(xs, b)
# return _bisection(xs, a, b, fa, fb)
# prev_x, prev_f = x, fx
# # If still not found, raise - likely no real root within searched domain
# raise ValueError("Failed to find a real root in searching domain.")