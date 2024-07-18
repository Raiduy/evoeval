from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings a and b, and return result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    result = ''
    if len(a) < len(b):
        a = a.zfill(len(b))
    elif len(b) < len(a):
        b = b.zfill(len(a))
    for i in range(len(a)):
        result += str(int(a[i]) ^ int(b[i]))
    return result