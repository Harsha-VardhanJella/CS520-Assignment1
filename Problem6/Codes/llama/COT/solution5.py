from typing import List

def factorize(n: int) -> List[int]:
    """
    Return the list of prime factors of n from smallest to largest.
    Each prime appears as many times as in the factorization.
    """
    factors = []
    i = 2
    #Removed induced Bug
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors