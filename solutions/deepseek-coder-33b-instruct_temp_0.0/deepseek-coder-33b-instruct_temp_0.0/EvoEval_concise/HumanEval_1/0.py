from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ 
    Takes a string of multiple balanced and non-nested parentheses groups. Returns a list containing each group as a separate string. Spaces within the string are ignored.
    
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(' ', '')
    groups = []
    start = 0
    count = 0
    for (i, char) in enumerate(paren_string):
        if char == '(':
            if count == 0:
                start = i
            count += 1
        elif char == ')':
            count -= 1
            if count == 0:
                groups.append(paren_string[start:i + 1])
    return groups