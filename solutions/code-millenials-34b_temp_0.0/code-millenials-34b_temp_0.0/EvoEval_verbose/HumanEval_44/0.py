

def change_base(x: int, base: int):
    """
    Convert and change the numerical base of a given input number 'x' into a different base 'base'.
    """
    if x < 0:
        raise ValueError('Negative numbers are not supported.')
    if base < 2 or base > 9:
        raise ValueError('Only bases between 2 and 9 are supported.')
    convertString = '0123456789'
    result = ''
    while x > 0:
        result = convertString[x % base] + result
        x = x // base
    return result