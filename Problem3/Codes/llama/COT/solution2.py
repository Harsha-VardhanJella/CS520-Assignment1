from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter the given list to include only integers.
    
    Args:
        values (List[Any]): A list containing elements of any type.
    
    Returns:
        List[int]: A list of integers filtered from the input list.
    """
    return [value for value in values if isinstance(value, int)]