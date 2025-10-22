from typing import List
import math

def factorize(n: int) -> List[int]:
    factors: List[int] = []
    if n <= 1:
        return factors
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        while n % f == 0:
            factors.append(f)
            n //= f
        f += 2
    if n > 1:
        factors.append(n)
    return factors
