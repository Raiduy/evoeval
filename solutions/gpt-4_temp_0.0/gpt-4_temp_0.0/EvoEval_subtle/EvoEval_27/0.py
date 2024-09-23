
def flip_case(string: str, exclusive_case: str='lower') -> str:
    """ For a given string, flip lowercase characters to uppercase and uppercase to lowercase, unless they are in exclusive_case which can be either 'lower' or 'upper'.
    If exclusive_case is 'lower', lowercase letters will remain as they are.
    If exclusive_case is 'upper', uppercase letters will remain as they are.
    >>> flip_case('Hello', 'lower')
    'hello'
    """
    result = ''
    for char in string:
        if exclusive_case == 'lower':
            if char.isupper():
                result += char.lower()
            else:
                result += char
        elif exclusive_case == 'upper':
            if char.islower():
                result += char.upper()
            else:
                result += char
    return result