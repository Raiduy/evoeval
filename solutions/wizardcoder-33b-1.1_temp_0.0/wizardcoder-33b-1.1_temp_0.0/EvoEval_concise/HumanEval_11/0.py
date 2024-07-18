from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings a and b, and return result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'
    return result