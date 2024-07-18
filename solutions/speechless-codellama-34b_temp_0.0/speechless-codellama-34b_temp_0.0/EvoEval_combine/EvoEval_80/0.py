def cyclic_encode_delete(s: str, c: str) -> tuple:
    encoded = ''
    for i in range(0, len(s), 3):
        group = s[i:i + 3]
        encoded += group[1] + group[2] + group[0]
    result = ''
    for char in encoded:
        if char not in c:
            result += char
    is_palindrome = result == result[::-1]
    if not is_palindrome:
        decoded = ''
        for i in range(0, len(result), 3):
            group = result[i:i + 3]
            decoded += group[2] + group[0] + group[1]
        result = decoded
    return (result, is_palindrome)