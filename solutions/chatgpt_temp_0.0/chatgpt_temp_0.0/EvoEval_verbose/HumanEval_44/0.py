

def change_base(x: int, base: int):
    """
    Convert and change the numerical base of a given input number 'x' into a different base 'base'.
    
    This function takes two arguments:
    1. 'x': an integer which represents the number you want to convert.
    2. 'base': an integer which represents the base to which you wish to convert 'x'.
    
    The function then converts 'x' to the desired 'base'.
    Note that the base numbers are expected to be less than 10.
    
    After conversion, the function does not return the resulting number as a numerical value. Instead,
    it returns a string that represents the number in the new base. This is done because the
    number may not be readable in the usual decimal system (for example, base 2 or binary numbers).
    
    Example:
    If you call change_base(8, 3), the function will convert the number 8 from base 10 to base 3,
    resulting in the number '22' which is a string, not a numerical value. Similarly, change_base(8, 2)
    will convert the number 8 from base 10 to base 2, resulting in '1000', and change_base(7, 2) will
    convert the number 7 to base 2, resulting in '111'.

    Here are some example usages of the function:
    >>> change_base(8, 3)
    '22'
    >>> change_base(8, 2)
    '1000'
    >>> change_base(7, 2)
    '111'
    """
    if x < 0 or base < 2 or base > 9:
        return 'Invalid input. x must be a non-negative integer and base must be between 2 and 9.'
    result = ''
    while x > 0:
        remainder = x % base
        result = str(remainder) + result
        x = x // base
    return result if result else '0'