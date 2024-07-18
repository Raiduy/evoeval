from typing import List, Tuple

def string_xor_advanced(a: str, b: str, c: str, rotation: Tuple[int, int]) -> str:
    a = rotate_string(a, rotation[0])
    b = rotate_string(b, rotation[1])
    c = rotate_string(c, rotation[1])
    result = int(a, 2) ^ int(b, 2) ^ int(c, 2)
    return format(result, 'b')