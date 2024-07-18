
def encode_shift(s: str, shift: int = 5):
    """
    returns encoded string by shifting every character by 'shift' in the alphabet.
    """
    return "".join([chr(((ord(ch) + shift - ord("a")) % 26) + ord("a")) for ch in s])


def decode_shift(s: str, shift: int=5) -> str:
    """
    takes as input string encoded with encode_shift function. Returns decoded string by reversing the shift.
    """
    return ''.join([chr((ord(ch) - ord('a') - shift) % 26 + ord('a')) for ch in s])