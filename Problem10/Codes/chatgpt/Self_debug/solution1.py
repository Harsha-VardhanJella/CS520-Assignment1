from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    result = []
    balance = 0
    current = ''
    for ch in paren_string.replace(' ', ''):
        current += ch
        if ch == '(':
            balance += 1
        elif ch == ')':
            balance -= 1
        if balance == 0 and current:
            result.append(current)
            current = ''
    return result
