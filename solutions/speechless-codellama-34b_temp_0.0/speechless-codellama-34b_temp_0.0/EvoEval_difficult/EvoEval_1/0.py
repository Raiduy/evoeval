from typing import List, Tuple

def separate_paren_groups(paren_string: str, remove_unbalanced: bool=False) -> Tuple[List[str], int]:
    groups = []
    unbalanced_count = 0
    current_group = ''
    open_count = 0
    for char in paren_string:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
        if char == ' ' and open_count == 0:
            if remove_unbalanced and open_count != 0:
                unbalanced_count += 1
            else:
                groups.append(current_group)
                current_group = ''
        elif char != ' ':
            current_group += char
    if remove_unbalanced and open_count != 0:
        unbalanced_count += 1
    else:
        groups.append(current_group)
    return (groups, unbalanced_count)