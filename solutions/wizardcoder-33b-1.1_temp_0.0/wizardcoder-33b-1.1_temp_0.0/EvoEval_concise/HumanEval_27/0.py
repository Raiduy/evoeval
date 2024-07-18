

def flip_case(string: str) -> str:
    """ Switches the case of each character in the given string.
    >>> flip_case('Hello')
    'hELLO'
    """
    return ''.join([char.upper() if char.islower() else char.lower() for char in string])