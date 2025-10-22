from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (length >= 2), select and return two that are the closest to each other.
    Return them as a tuple in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        raise ValueError("numbers must contain at least two elements")
    sorted_nums = sorted(numbers)
    min_diff = float("inf")
    best_pair = (sorted_nums[0], sorted_nums[1])
    for i in range(len(sorted_nums) - 1):
        a = sorted_nums[i]
        b = sorted_nums[i + 1]
        diff = b - a  # non-negative because list is sorted
        if diff < min_diff:
            min_diff = diff
            best_pair = (a, b)
    return best_pair
