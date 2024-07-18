from typing import List


def string_xor(a: str, b: str) -> str:
    xor_result = int(a, 2) ^ int(b, 2)
    binary_result = bin(xor_result)[2:]
    return binary_result[::-1]