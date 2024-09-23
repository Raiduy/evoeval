def cyclic_encode_delete(s: str, c: str) -> tuple:

    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    def encode(s: str) -> str:
        encoded = ''
        for i in range(0, len(s), 3):
            group = s[i:i + 3]
            encoded += group[1:] + group[:1]
        return encoded

    def decode(s: str) -> str:
        decoded = ''
        for i in range(0, len(s), 3):
            group = s[i:i + 3]
            decoded += group[-1:] + group[:-1]
        return decoded
    encoded_s = encode(s)
    result = ''.join([ch for ch in encoded_s if ch not in c])
    if is_palindrome(result):
        return (result, True)
    else:
        return (decode(result), False)