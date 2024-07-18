def cyclic_encode_delete(s: str, c: str) -> tuple:

    def encode(s: str) -> str:
        return s[2:] + s[:2]

    def decode(s: str) -> str:
        return s[-2:] + s[:-2]

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]
    encoded = ''.join((encode(s[i:i + 3]) for i in range(0, len(s), 3)))
    result = ''.join((ch for ch in encoded if ch not in c))
    if is_palindrome(result):
        return (result, True)
    else:
        return (''.join((decode(result[i:i + 3]) for i in range(0, len(result), 3))), False)