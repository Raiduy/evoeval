from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Perform binary XOR on two binary strings a and b, and return result as a string.
    >>> string_xor('010', '110')
    '100'
    """
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    for i in range(max_len):
        result += str(int(a[i]) ^ int(b[i]))
    return result