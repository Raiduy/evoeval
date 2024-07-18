
def encode_shift(s: str):
    """
    returns encoded string by shifting every character by 5 in the alphabet.
    """
    return "".join([chr(((ord(ch) + 5 - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str):
    """
    This function, 'decode_shift', accepts a single argument 's', which is a string data type. 
    The input string 's' is assumed to have been previously encoded using a specific function named 'encode_shift'. 

    The purpose of this function is to revert the encoding that was performed by 'encode_shift' function. 
    This is done by applying the same logic as 'encode_shift', but in reverse, to decode the string. As a result, it returns 
    the original, unaltered string, effectively undoing the encoding process. 
    """
    return ''.join([chr((ord(ch) - ord('a') - 5) % 26 + ord('a')) for ch in s])