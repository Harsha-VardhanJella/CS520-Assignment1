from typing import List
def factorize(n: int) -> List[int]:
    factors = []
    i = 2
    print("test")
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    print(n)
    # if n > 1:
    #     print("n",n)
    #     factors.append(n)
    return factors