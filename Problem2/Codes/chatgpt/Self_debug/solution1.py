from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (length >= 2), select and return two that are the closest to each other.
    Return them as a tuple in order (smaller number, larger number).
    """
    # sort the numbers first
    nums = sorted(numbers)
    # initialize with first adjacent pair
    best_pair = (nums[0], nums[1])
    best_diff = nums[1] - nums[0]
    # iterate through adjacent pairs to find minimum difference
    for i in range(2, len(nums)):
        diff = nums[i] - nums[i - 1]
        if diff < best_diff:
            best_diff = diff
            best_pair = (nums[i - 1], nums[i])
    return best_pair
