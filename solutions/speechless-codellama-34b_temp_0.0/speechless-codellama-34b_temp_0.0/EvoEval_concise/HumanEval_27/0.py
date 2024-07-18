

def flip_case(string: str) -> str:
    """ Switches the case of each character in the given string.
    >>> flip_case('Hello')
    'hELLO'
    """
    result = ''
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result