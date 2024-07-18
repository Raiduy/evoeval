from typing import List, Tuple

def string_xor_advanced(a: str, b: str, c: str, rotation: Tuple[int, int]) -> str:
    a = a[-rotation[0]:] + a[:-rotation[0]]
    b = b[-rotation[1]:] + b[:-rotation[1]]
    c = c[-rotation[1]:] + c[:-rotation[1]]
    xor_ab = ''.join((str(int(a[i]) ^ int(b[i])) for i in range(len(a))))
    xor_abc = ''.join((str(int(xor_ab[i]) ^ int(c[i])) for i in range(len(xor_ab))))
    return xor_abc