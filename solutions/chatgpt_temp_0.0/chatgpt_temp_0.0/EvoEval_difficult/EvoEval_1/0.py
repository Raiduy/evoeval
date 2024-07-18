from typing import List, Tuple

def separate_paren_groups(paren_string: str, remove_unbalanced: bool=False) -> Tuple[List[str], int]:
    groups = []
    current_group = ''
    count_unbalanced = 0
    open_count = 0
    for char in paren_string:
        if char == '(':
            open_count += 1
            current_group += char
        elif char == ')':
            if open_count > 0:
                open_count -= 1
                current_group += char
            elif remove_unbalanced:
                count_unbalanced += 1
        elif char == ' ':
            if current_group:
                groups.append(current_group)
                current_group = ''
    if current_group:
        groups.append(current_group)
    return (groups, count_unbalanced)