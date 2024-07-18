def cyclic_encode_delete(s: str, c: str) -> tuple:

    def cycle(s: str) -> str:
        return s[1:] + s[0]

    def encode(s: str) -> str:
        return ''.join((cycle(s[i:i + 3]) for i in range(0, len(s), 3)))

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def delete(s: str, c: str) -> str:
        return ''.join((ch for ch in s if ch not in c))
    encoded = encode(s)
    deleted = delete(encoded, c)
    result = deleted if is_palindrome(deleted) else encode(deleted)
    return (result, is_palindrome(result))