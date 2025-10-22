from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """
    Check if in the given list of numbers, any two numbers are closer to each other than the given threshold.
    """
    if len(numbers) < 2:
        return False
    
    sorted_numbers = sorted(numbers)
    
    for i in range(len(sorted_numbers) - 1):
        if sorted_numbers[i + 1] - sorted_numbers[i] <= threshold:
            return True
            
    return False