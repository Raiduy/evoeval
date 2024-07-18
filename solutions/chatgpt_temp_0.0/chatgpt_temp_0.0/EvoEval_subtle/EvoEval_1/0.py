from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    stack = []
    groups = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
            if not stack:
                groups.append(paren_string[:paren_string.index(char) + 1])
                paren_string = paren_string[paren_string.index(char) + 1:]
    groups.sort()
    return groups