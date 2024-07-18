
def len_base_conversion(x: int, base: int) -> int:
    """ 
    Convert the numerical base of input number x to base and 
    return the length of string representation after the conversion. 
    base numbers are less than 10.
    
    >>> len_base_conversion(8, 3)
    2
    >>> len_base_conversion(8, 2)
    4
    >>> len_base_conversion(7, 2)
    3
    """
    if base < 2 or base > 10:
        raise ValueError('Base must be between 2 and 10')
    if x < 0:
        raise ValueError('x must be a non-negative integer')
    if x == 0:
        return 1
    length = 0
    while x > 0:
        x //= base
        length += 1
    return length