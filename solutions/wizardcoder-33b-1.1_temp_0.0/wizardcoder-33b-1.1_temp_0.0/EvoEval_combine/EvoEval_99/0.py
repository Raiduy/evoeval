
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
    if base == 10:
        return len(str(x))
    else:
        result = ''
        while x > 0:
            result = str(x % base) + result
            x //= base
        return len(result)