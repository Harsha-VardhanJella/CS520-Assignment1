from typing import List

def factorize(n: int) -> List[int]:
    """
    Return the list of prime factors of n from smallest to largest.
    Each prime appears as many times as in the factorization.
    For n < 2 returns an empty list.
    """
    if n < 2:
        return []
    factors: List[int] = []
    # handle factor 2
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    # handle odd factors
    i = 3
    while i * i <= n:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 2
    # if remaining n is prime
    if n > 1:
        factors.append(n)
    return factors
