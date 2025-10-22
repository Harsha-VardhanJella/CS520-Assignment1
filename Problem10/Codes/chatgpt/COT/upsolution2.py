
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    groups = []
    stack = []
    start_idx = 0

    for idx, char in enumerate(paren_string):
        if char == '(':
            if not stack:
                start_idx = idx
            stack.append(char)
        elif char == ')':
            stack.pop()
            if not stack:
                groups.append(paren_string[start_idx:idx+1])
    
    return groups
