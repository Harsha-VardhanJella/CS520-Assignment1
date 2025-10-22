from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (length >= 2), select and return two that are the closest to each other.
    Return them as a tuple in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        raise ValueError("numbers must contain at least two elements")
    nums = sorted(numbers)
    best_a, best_b = nums[0], nums[1]
    best_diff = abs(best_b - best_a)
    for i in range(1, len(nums)):
        a, b = nums[i - 1], nums[i]
        diff = abs(b - a)
        if diff < best_diff:
            best_diff = diff
            best_a, best_b = a, b
    return (best_a, best_b)
