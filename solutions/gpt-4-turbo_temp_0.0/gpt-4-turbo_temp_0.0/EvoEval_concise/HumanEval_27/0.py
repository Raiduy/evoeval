

def flip_case(string: str) -> str:
    """ Switches the case of each character in the given string.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_string = [char.lower() if char.isupper() else char.upper() for char in string]
    return ''.join(flipped_string)