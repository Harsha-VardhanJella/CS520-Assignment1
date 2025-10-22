from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return the list of prime factors of n from smallest to largest.
    Each prime appears as many times as in the factorization.
    For n == 0 a ValueError is raised. For |n| < 2 an empty list is returned.
    """
    if n == 0:
        raise ValueError("factorization of 0 is undefined")
    m = abs(n)
    if m < 2:
        return []
    factors: List[int] = []
    # factor out 2s
    while m % 2 == 0:
        factors.append(2)
        m //= 2
    # factor odd primes
    f = 3
    while f * f <= m:
        while m % f == 0:
            factors.append(f)
            m //= f
        f += 2
    if m > 1:
        factors.append(m)
    return factors
