
def flip_case(string: str, exclusive_case: str='lower') -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase, unless they are in exclusive_case which can be either 'lower' or 'upper'.
    If exclusive_case is 'lower', lowercase letters will remain as they are.
    If exclusive_case is 'upper', uppercase letters will remain as they are.
    >>> flip_case('Hello', 'lower')
    'hello'
    """
    flipped_string = ''
    for char in string:
        if char.islower() and exclusive_case != 'lower':
            flipped_string += char.upper()
        elif char.isupper() and exclusive_case != 'upper':
            flipped_string += char.lower()
        else:
            flipped_string += char
    return flipped_string