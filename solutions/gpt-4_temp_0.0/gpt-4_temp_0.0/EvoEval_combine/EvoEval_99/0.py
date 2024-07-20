
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
    converted_number = ''
    while x > 0:
        (x, remainder) = divmod(x, base)
        converted_number = str(remainder) + converted_number
    return len(converted_number)