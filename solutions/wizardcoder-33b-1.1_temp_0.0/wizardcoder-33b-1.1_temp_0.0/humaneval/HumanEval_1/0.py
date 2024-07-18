from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    paren_string = paren_string.replace(" ", "")
    stack = []
    result = []
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            temp = ''
            while stack and stack[-1] != '(':
                temp = stack.pop() + temp
            stack.pop()  # pop the '('
            stack.append(temp)
        else:
            stack.append(char)
    while stack:
        result.append(stack.pop())
    return result

