def check_validity(input_string: str) -> bool:
    """Check if the input string is a valid binary representation.

    A valid binary representation contains only the digits 0 and 1.
    Returns True if the string is valid and False otherwise.

    >>> check_validity('0101')
    True
    >>> check_validity('1234')
    False
    >>> check_validity('ABCD')
    False
    """
    valid_digits = {'0', '1'}
    return set(input_string) <= valid_digits
def binary_to_decimal(binary_string: str) -> int:
    """Convert a binary string to a decimal number.

    The string must represent a valid binary number, 
    i.e., it should contain only the digits 0 and 1.
    If the string is not valid, return -1.
    If the string is empty, return None.

    >>> binary_to_decimal('1101')
    13
    >>> binary_to_decimal('1000')
    8
    >>> binary_to_decimal('')
    None
    >>> binary_to_decimal('1234')
    -1
    """
    if binary_string == '':
        return None
    elif check_validity(binary_string):
        return int(binary_string, 2)
    else:
        return -1