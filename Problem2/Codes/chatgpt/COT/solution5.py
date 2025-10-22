from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (length >= 2), select and return two that are the closest to each other.
    Return them as a tuple in order (smaller number, larger number).
    """
    if len(numbers) < 2:
        raise ValueError("numbers must contain at least two elements")
    if len(numbers) == 2:
        a, b = numbers[0], numbers[1]
        return (a, b) if a <= b else (b, a)

    sorted_nums = sorted(numbers)
    best_pair = (sorted_nums[0], sorted_nums[1])
    best_diff = abs(best_pair[1] - best_pair[0])

    # tolerance for floating point tie-comparison
    tol = 1e-12

    for i in range(1, len(sorted_nums) - 0):
        if i >= len(sorted_nums):
            break
        a, b = sorted_nums[i - 1], sorted_nums[i]
        diff = abs(b - a)
        if diff + tol < best_diff:  # strictly better
            best_diff = diff
            best_pair = (a, b)
        elif abs(diff - best_diff) <= tol:
            # tie-break: choose lexicographically smaller pair (smaller first element, then smaller second)
            if (a, b) < best_pair:
                best_pair = (a, b)

    return best_pair
