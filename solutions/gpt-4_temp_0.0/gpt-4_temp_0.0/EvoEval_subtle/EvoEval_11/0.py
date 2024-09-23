from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string but reversed.
    >>> string_xor('010', '110')
    '001'
    """
    max_len = max(len(a), len(b))
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = [str(int(a[i]) ^ int(b[i])) for i in range(max_len)]
    return ''.join(result[::-1])