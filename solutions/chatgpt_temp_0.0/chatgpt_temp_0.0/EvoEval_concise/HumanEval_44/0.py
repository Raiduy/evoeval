def change_base(x: int, base: int):
    """Converts integer x to a different numerical base.
    Returns the conversion as a string.
    The base is less than 10.
    """
    if x < 0 or base < 2 or base > 9:
        return 'Invalid input'
    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result