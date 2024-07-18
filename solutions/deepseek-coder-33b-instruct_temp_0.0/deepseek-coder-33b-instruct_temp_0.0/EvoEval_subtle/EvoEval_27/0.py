
def flip_case(string: str, exclusive_case: str='lower') -> str:
    """
    For a given string, flip lowercase characters to uppercase and uppercase to lowercase, unless they are in exclusive_case which can be either 'lower' or 'upper'.
    If exclusive_case is 'lower', lowercase letters will remain as they are.
    If exclusive_case is 'upper', uppercase letters will remain as they are.
    >>> flip_case('Hello', 'lower')
    'hello'
    """
    result = ''
    for char in string:
        if char.islower() and exclusive_case == 'lower':
            result += char
        elif char.isupper() and exclusive_case == 'upper':
            result += char
        elif char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result