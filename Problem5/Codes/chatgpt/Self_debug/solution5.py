def largest_divisor(n: int) -> int:
    #Bug induced
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            return i
