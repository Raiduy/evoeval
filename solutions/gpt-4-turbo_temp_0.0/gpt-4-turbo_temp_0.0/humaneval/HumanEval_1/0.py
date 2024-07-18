from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces from the input string
    paren_string = paren_string.replace(" ", "")
    
    # List to store the separate groups
    groups = []
    
    # Temporary string to build the current group
    current_group = ""
    
    # Counter to keep track of the balance of parentheses
    balance = 0
    
    # Iterate through each character in the string
    for char in paren_string:
        # If it's an opening parenthesis, increase the balance and add to the current group
        if char == '(':
            balance += 1
            current_group += char
        # If it's a closing parenthesis, decrease the balance and add to the current group
        elif char == ')':
            balance -= 1
            current_group += char
            
            # If the balance is 0, we've completed a group
            if balance == 0:
                groups.append(current_group)
                current_group = ""
    
    return groups
