

def flip_case(string: str) -> str:
    """ Switches the case of each character in the given string.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join((char.lower() if char.isupper() else char.upper() for char in string))