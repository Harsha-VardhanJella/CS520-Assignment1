
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    groups = []
    stack = 0
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            stack += 1
        if stack > 0:
            current_group += char
        if char == ')':
            stack -= 1
            if stack == 0:
                groups.append(current_group)
                current_group = ""
                
    return groups
