from typing import List


def string_xor(a: str, b: str) -> str:
    result = []
    for i in range(len(a)):
        if a[i] == b[i]:
            result.append('0')
        else:
            result.append('1')
    return ''.join(result[::-1])