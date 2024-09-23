from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ 
    Takes a string of multiple balanced and non-nested parentheses groups. Returns a list containing each group as a separate string. Spaces within the string are ignored.
    
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    stack = []
    result = []
    group = ''
    for char in paren_string:
        if char == '(':
            if group:
                stack.append(group)
                group = ''
            group += char
        elif char == ')':
            group += char
            if stack:
                group = stack.pop() + group
            result.append(group)
            group = ''
    return result