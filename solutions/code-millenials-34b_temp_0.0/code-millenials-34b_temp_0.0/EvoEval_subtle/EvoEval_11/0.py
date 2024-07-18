from typing import List


def string_xor(a: str, b: str) -> str:
    xor_result = ''.join((str(int(x) ^ int(y)) for (x, y) in zip(a, b)))
    return xor_result[::-1]