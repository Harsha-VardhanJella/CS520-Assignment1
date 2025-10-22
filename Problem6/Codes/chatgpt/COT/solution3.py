from typing import List
import math

def factorize(n: int) -> List[int]:
    """
    Return the list of prime factors of n from smallest to largest.
    Each prime appears as many times as in the factorization.
    For n < 2 an empty list is returned.
    """
    factors: List[int] = []
    if n < 2:
        return factors

    # Handle factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Handle odd factors
    p = 3
    while p * p <= n:
        while n % p == 0:
            factors.append(p)
            n //= p
        p += 2

    # If remaining n is a prime > 1
    if n > 1:
        factors.append(n)

    return factors
