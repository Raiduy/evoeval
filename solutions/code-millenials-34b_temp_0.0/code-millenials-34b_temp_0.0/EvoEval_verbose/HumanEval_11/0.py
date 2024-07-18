from typing import List


def string_xor(a: str, b: str) -> str:
    if len(a) != len(b):
        raise ValueError('Input strings must be of equal length')
    result = ''
    for (char_a, char_b) in zip(a, b):
        if char_a not in '01' or char_b not in '01':
            raise ValueError("Input strings must contain only '1's and '0's")
        result += str(int(char_a) ^ int(char_b))
    return result