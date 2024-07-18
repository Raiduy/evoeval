

def change_base(x: int, base: int) -> int:
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
    result = 0
    power = 0
    while x > 0:
        remainder = x % base
        result += remainder * 10 ** power
        x //= base
        power += 1
    return result