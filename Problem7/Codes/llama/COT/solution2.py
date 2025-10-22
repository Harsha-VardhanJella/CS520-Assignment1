from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    """
    From a list of integers, remove all elements that occur more than once.
    Keep the order of the remaining elements the same as in the input.
    """
    count = Counter(numbers)
    return [num for num in numbers if count[num] == 1]