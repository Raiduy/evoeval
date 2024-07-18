from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            group = ''
            while stack and stack[-1] != '(':
                group = stack.pop() + group
            stack.pop()
            result.append('(' + group + ')')
    return sorted(result)