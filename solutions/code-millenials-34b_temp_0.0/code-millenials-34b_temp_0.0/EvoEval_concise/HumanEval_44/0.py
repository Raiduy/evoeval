def change_base(x: int, base: int):
    """Converts integer x to a different numerical base.
    Returns the conversion as a string.
    The base is less than 10.

    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x < 0:
        return '-' + change_base(-x, base)
    elif x < base:
        return str(x)
    else:
        return change_base(x // base, base) + str(x % base)