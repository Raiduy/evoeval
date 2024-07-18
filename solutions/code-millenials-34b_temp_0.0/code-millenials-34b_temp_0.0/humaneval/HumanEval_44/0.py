

def change_base(x: int, base: int):
    """Change numerical base of input number x to base.
    return string representation after the conversion.
    base numbers are less than 10.
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x < 0:
        raise ValueError("Input number must be a positive integer.")
    if base < 0 or base >= 10:
        raise ValueError("Base must be an integer between 0 and 9.")

    digits = "0123456789"
    result = ""
    while x > 0:
        result = digits[x % base] + result
        x //= base
    return result
