from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (length >= 2), select and return two that are the closest to each other.
    Return them as a tuple in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        raise ValueError("numbers must contain at least two elements")
    sorted_nums = sorted(numbers)
    best_pair = (sorted_nums[0], sorted_nums[1])
    min_diff = sorted_nums[1] - sorted_nums[0]
    for i in range(2, len(sorted_nums)):
        diff = sorted_nums[i] - sorted_nums[i - 1]
        if diff < min_diff:
            min_diff = diff
            best_pair = (sorted_nums[i - 1], sorted_nums[i])
    return best_pair
