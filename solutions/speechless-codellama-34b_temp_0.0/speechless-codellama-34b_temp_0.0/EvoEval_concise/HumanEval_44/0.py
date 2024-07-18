def change_base(x: int, base: int) -> str:
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
    result = []
    while x > 0:
        result.append(str(x % base))
        x //= base
    return ''.join(result[::-1])