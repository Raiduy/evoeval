from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(' ', '')
    stack = []
    groups = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            group = ''
            while stack[-1] != '(':
                group = stack.pop() + group
            stack[-1] = '(' + group + ')'
            groups.append(stack.pop())
    return sorted(groups)