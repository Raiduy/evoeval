

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return integer representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    22
    >>> change_base(8, 2)
    1000
    >>> change_base(7, 2)
    111
    """
    if x == 0:
        return 0
    else:
        return x % base + 10 * change_base(x // base, base)