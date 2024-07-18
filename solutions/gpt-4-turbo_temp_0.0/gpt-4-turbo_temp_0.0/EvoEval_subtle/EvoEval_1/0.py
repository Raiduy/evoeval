from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    separated_groups = []
    balance = 0
    current_group = ''
    for char in paren_string:
        current_group += char
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance == 0:
            separated_groups.append(current_group)
            current_group = ''
    separated_groups.sort()
    return separated_groups