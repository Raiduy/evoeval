from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings a and b, and return result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    if len(a) != len(b):
        raise ValueError('Both strings must have the same length')
    result = ''.join((str(int(x) ^ int(y)) for (x, y) in zip(a, b)))
    return result