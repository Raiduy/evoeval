from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ 
    Takes a string of multiple balanced and non-nested parentheses groups. Returns a list containing each group as a separate string. Spaces within the string are ignored.
    
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    groups = []
    current_group = []
    open_count = 0
    for char in paren_string:
        if char == '(':
            open_count += 1
            current_group.append(char)
        elif char == ')':
            open_count -= 1
            current_group.append(char)
            if open_count == 0:
                groups.append(''.join(current_group))
                current_group = []
    return groups