

def flip_case(string: str) -> str:
    """ Switches the case of each character in the given string.
    >>> flip_case('Hello')
    'hELLO'
    """
    flipped_string = ''
    for char in string:
        if char.islower():
            flipped_string += char.upper()
        else:
            flipped_string += char.lower()
    return flipped_string