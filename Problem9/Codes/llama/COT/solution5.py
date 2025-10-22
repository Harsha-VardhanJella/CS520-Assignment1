from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the given list of numbers, any two numbers are closer to each other than the given threshold.
    """
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i + 1] - numbers[i] <= threshold:
            return True
    return False