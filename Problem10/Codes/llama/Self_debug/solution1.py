from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    groups = []
    current_group = ""
    balance = 0
    
    for char in paren_string:
        if char == "(":
            current_group += char
            balance += 1
        elif char == ")":
            current_group += char
            balance -= 1
            if balance == 0:
                groups.append(current_group)
                current_group = ""
        elif char == " ":
            if current_group:
                current_group += char
    
    result = [group for group in groups if group.strip()]
    return result