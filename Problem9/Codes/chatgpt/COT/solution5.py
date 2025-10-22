from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    numbers_sorted = sorted(numbers)
    for i in range(1, len(numbers_sorted)):
        if abs(numbers_sorted[i] - numbers_sorted[i - 1]) < threshold:
            return True
    return False
