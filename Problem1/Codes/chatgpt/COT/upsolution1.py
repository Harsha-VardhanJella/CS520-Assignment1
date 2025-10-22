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
    if not xs:
        raise ValueError("Coefficient list xs must not be empty.")
    if all(c == 0 for c in xs):
        return 0.0

    tol = 1e-12
    max_expand = 60
    max_bisect = 200

    # Initial bracket centered at 0 with growing radius
    radius = 1.0
    a, b = -radius, radius
    fa, fb = poly(xs, a), poly(xs, b)

    if fa == 0.0:
        return a
    if fb == 0.0:
        return b

    expands = 0
    while fa * fb > 0.0 and expands < max_expand:
        radius *= 2.0
        a, b = -radius, radius
        fa, fb = poly(xs, a), poly(xs, b)
        if fa == 0.0:
            return a
        if fb == 0.0:
            return b
        expands += 1

    if fa * fb > 0.0:
        raise ValueError("Failed to bracket a root within expansion limit.")

    # Bisection
    left, right = a, b
    f_left, f_right = fa, fb
    for _ in range(max_bisect):
        mid = 0.5 * (left + right)
        f_mid = poly(xs, mid)

        if f_mid == 0.0 or 0.5 * (right - left) < tol * max(1.0, abs(mid)):
            return mid

        if f_left * f_mid < 0.0:
            right, f_right = mid, f_mid
        else:
            left, f_left = mid, f_mid

    return 0.5 * (left + right)
