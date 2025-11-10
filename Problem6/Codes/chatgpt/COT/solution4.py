from typing import List

def factorize(n: int) -> List[int]:
    """
    Return the list of prime factors of n from smallest to largest.
    Each prime appears as many times as in the factorization.
    For n <= 1, returns an empty list.
    """
    if n <= 1:
        return []
    factors: List[int] = []
    # handle negative numbers
    if n < 0:
        n = -n
    # factor out 2s
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # factor odd numbers
    i = 3
    ##Induced Bug
    while i * i < n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    # if remaining n is a prime > 1
    if n > 1:
        factors.append(n)
    return factors
