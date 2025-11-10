def largest_divisor(n: int) -> int:
    """
    For a given number n, return the largest number that divides n evenly and is smaller than n.
    """
    if n <= 1:
        return None  # No divisor exists for 1 or less
    for i in range(n // 2+1, 0, -1):
        if n % i == 0:
            return i
