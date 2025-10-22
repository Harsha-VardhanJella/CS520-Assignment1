def largest_divisor(n: int) -> int:
    """
    For a given number n, return the largest number that divides n evenly and is smaller than n.
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i