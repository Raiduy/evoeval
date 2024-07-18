from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string but reversed.
    >>> string_xor('010', '110')
    '001'
    """
    assert len(a) == len(b), 'Input strings must be of equal length'
    xor_result = ''.join((str(int(x) ^ int(y)) for (x, y) in zip(a, b)))
    return xor_result[::-1]