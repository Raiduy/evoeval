
def flip_case(string: str, exclusive_case: str='lower') -> str:
    result = ''
    for char in string:
        if char.isupper() and exclusive_case != 'upper':
            result += char.lower()
        elif char.islower() and exclusive_case != 'lower':
            result += char.upper()
        else:
            result += char
    return result