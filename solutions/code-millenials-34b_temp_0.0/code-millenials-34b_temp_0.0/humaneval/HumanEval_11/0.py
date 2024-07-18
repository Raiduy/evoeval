from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Initialize an empty string to store the result
    result = ''
    
    # Ensure both strings are of equal length
    # If they are not, pad the shorter string with 0s at the beginning
    if len(a) < len(b):
        a = a.zfill(len(b))
    elif len(b) < len(a):
        b = b.zfill(len(a))
    
    # Perform XOR operation on the characters of the strings
    for i in range(len(a)):
        # XOR operation
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    
    return result
