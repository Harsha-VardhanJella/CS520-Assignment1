def largest_divisor(n: int) -> int:
    #removed induced bug
    for i in range(n // 2, 0, -1):
        if n % i == 0:
            return i
