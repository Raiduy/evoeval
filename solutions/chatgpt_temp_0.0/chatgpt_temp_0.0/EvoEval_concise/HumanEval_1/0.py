from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Takes a string of multiple balanced and non-nested parentheses groups. Returns a list containing each group as a separate string. Spaces within the string are ignored.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    result = []
    stack = []
    current_group = ''
    for char in paren_string:
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        current_group += char
        if not stack:
            result.append(current_group.strip())
            current_group = ''
    return result