def cyclic_encode_delete(s: str, c: str) -> tuple:

    def encode(s: str) -> str:
        return s[2:] + s[:2]

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def decode(s: str) -> str:
        return s[1:] + s[0]
    encoded = ''.join((encode(s[i:i + 3]) for i in range(0, len(s), 3)))
    filtered = ''.join((ch for ch in encoded if ch not in c))
    is_palindrome_result = is_palindrome(filtered)
    if is_palindrome_result:
        return (filtered, is_palindrome_result)
    else:
        decoded = ''.join((decode(filtered[i:i + 3]) for i in range(0, len(filtered), 3)))
        return (decoded, is_palindrome_result)