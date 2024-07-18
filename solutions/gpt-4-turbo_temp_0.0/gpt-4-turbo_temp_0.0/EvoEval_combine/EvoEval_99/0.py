
def len_base_conversion(x: int, base: int) -> int:
    """ 
    Convert the numerical base of input number x to base and 
    return the length of string representation after the conversion. 
    base numbers are less than 10.
    """
    converted_str = ''
    if x == 0:
        return 1
    while x > 0:
        remainder = x % base
        x = x // base
        converted_str = str(remainder) + converted_str
    return len(converted_str)