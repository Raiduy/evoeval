from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check if the lengths of the strings are equal
    if len(a) != len(b):
        raise ValueError("Both strings must have the same length")

    # Perform XOR operation on each pair of corresponding characters
    result = ''.join(str(int(x) ^ int(y)) for x, y in zip(a, b))

    return result
