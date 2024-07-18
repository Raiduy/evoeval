from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings a and b, and return result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    a_int = int(a, 2)
    b_int = int(b, 2)
    result_int = a_int ^ b_int
    result_str = bin(result_int)[2:]
    return result_str