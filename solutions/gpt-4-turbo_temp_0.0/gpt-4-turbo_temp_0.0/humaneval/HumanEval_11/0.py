from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Ensure both strings are of the same length
    max_length = max(len(a), len(b))
    a = a.zfill(max_length)
    b = b.zfill(max_length)
    
    # Perform XOR operation on each pair of bits and collect the results
    result = ''.join(str(int(char_a) ^ int(char_b)) for char_a, char_b in zip(a, b))
    
    return result
