from typing import List
from collections import Counter

def remove_duplicates(numbers: List[int]) -> List[int]:
    counts = Counter(numbers)
    return [num for num in numbers if counts[num] == 1]
