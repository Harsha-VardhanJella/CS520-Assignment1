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
            if balance == 0:
                current_group = []
            current_group.append(char)
            balance += 1
        elif char == ')':
            current_group.append(char)
            balance -= 1
            if balance == 0:
                groups.append(''.join(current_group))
        else:
            if balance > 0:
                current_group.append(char)

    return groups
