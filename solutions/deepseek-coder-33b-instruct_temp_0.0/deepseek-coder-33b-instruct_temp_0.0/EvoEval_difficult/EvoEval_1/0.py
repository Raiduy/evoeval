from typing import List, Tuple

def separate_paren_groups(paren_string: str, remove_unbalanced: bool=False) -> Tuple[List[str], int]:
    stack = []
    groups = []
    unbalanced_count = 0
    current_group = ''
    for char in paren_string:
        if char == '(':
            stack.append(char)
            current_group += char
        elif char == ')':
            if stack:
                stack.pop()
                current_group += char
            else:
                unbalanced_count += 1
                if not remove_unbalanced:
                    current_group += char
        elif char == ' ':
            continue
        elif stack:
            current_group += char
        else:
            unbalanced_count += 1
            if not remove_unbalanced:
                current_group += char
        if not stack and current_group:
            groups.append(current_group)
            current_group = ''
    if stack:
        unbalanced_count += len(stack)
    return (groups, unbalanced_count)