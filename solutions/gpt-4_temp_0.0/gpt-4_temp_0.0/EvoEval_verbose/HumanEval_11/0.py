from typing import List


def string_xor(a: str, b: str) -> str:
    """ 
    The function string_xor takes two string arguments, a and b, which are both binary representations consisting solely of 1s and 0s.
    
    The purpose of this function is to perform a binary XOR (exclusive OR) operation on these input strings. 
    
    Each digit in the corresponding position of the strings a and b will be compared and the XOR operation will be applied.
    
    If the digits are the same (both 1s or both 0s), the resulting digit in the output string is '0'.
    If the digits are different (one is a 1 and the other is a 0), the resulting digit in the output string is '1'.
    
    The result of this operation string_xor(a, b) is also a binary string which is returned by the function.

    For example, if we call string_xor('010', '110'), the result will be '100' as the second and third digits of the
    input strings are the same (1 and 0 respectively), but the first digits are different (0 and 1).
    
    """
    assert len(a) == len(b), 'Both strings must be of the same length'
    result = ''.join(('1' if a[i] != b[i] else '0' for i in range(len(a))))
    return result