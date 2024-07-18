from typing import List, Tuple

def separate_paren_groups(paren_string: str, remove_unbalanced: bool=False) -> Tuple[List[str], int]:
    stack = []
    result = []
    unbalanced_count = 0
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack:
                if remove_unbalanced:
                    unbalanced_count += 1
                else:
                    result.append(')')
            else:
                stack.pop()
                if not stack:
                    result.append(''.join(stack))
                    stack = []
    if stack:
        if remove_unbalanced:
            unbalanced_count += len(stack)
        else:
            result.extend(stack)
    return (result, unbalanced_count)