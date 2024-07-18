from typing import List, Tuple

def separate_paren_groups(paren_string: str, remove_unbalanced: bool=False) -> Tuple[List[str], int]:
    groups = []
    current_group = []
    balance = 0
    removed_count = 0
    for char in paren_string:
        if char == '(':
            balance += 1
            current_group.append(char)
        elif char == ')':
            if balance > 0:
                balance -= 1
                current_group.append(char)
                if balance == 0:
                    groups.append(''.join(current_group))
                    current_group = []
            else:
                if remove_unbalanced:
                    removed_count += 1
                balance = 0
                current_group = []
    if balance != 0 and remove_unbalanced:
        removed_count += 1
    return (groups, removed_count)