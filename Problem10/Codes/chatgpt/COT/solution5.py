from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input is a string containing multiple groups of nested parentheses.
    Return the list of individual string groups.
    """
    groups = []
    stack = []
    current_group = []
    
    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group.append(char)
        elif char == ')':
            current_group.append(char)
            stack.pop()
            if not stack:
                groups.append(''.join(current_group))
                current_group = []
        elif stack:
            current_group.append(char)
    
    return groups
