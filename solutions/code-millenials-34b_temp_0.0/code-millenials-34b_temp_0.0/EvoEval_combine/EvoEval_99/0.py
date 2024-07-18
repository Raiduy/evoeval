
def len_base_conversion(x: int, base: int) -> int:
    if x < 0:
        raise ValueError('x must be a non-negative integer')
    if base < 2 or base > 9:
        raise ValueError('base must be an integer between 2 and 9')
    converted_x = ''
    while x > 0:
        converted_x = str(x % base) + converted_x
        x = x // base
    return len(converted_x)