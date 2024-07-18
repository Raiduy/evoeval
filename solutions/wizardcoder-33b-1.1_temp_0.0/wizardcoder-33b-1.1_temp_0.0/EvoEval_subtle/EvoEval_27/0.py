
def flip_case(string: str, exclusive_case: str='lower') -> str:
    result = ''
    for char in string:
        if exclusive_case == 'lower' and char.isupper():
            result += char.lower()
        elif exclusive_case == 'upper' and char.islower():
            result += char.upper()
        else:
            result += char.swapcase()
    return result