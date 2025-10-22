from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input is a string containing multiple groups of nested parentheses.
    Return the list of individual string groups.
    """
    groups = []
    current_group = []
    balance = 0
    
    for char in paren_string:
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            balance -= 1
            current_group.append(char)
            if balance == 0:
                groups.append(''.join(current_group))
                current_group = []
        else:
            if balance > 0:
                current_group.append(char)
    
    return groups
