from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input is a string containing multiple groups of nested parentheses.
    Returns a list of individual string groups.
    """
    groups = []
    stack = []
    current_group = ""
    
    for char in paren_string:
        if char == '(':
            if not stack:
                current_group = ""
            stack.append(char)
            current_group += char
        elif char == ')':
            if stack:
                stack.pop()
                current_group += char
                if not stack:
                    groups.append(current_group)
        else:
            if stack:
                current_group += char
    
    return groups
