def cyclic_encode_delete(s: str, c: str) -> tuple:
    encoded = ''
    for i in range(0, len(s), 3):
        if i + 2 < len(s):
            encoded += s[i + 1:i + 3] + s[i]
        else:
            encoded += s[i:]
    for char in c:
        encoded = encoded.replace(char, '')

    def is_palindrome(string):
        return string == string[::-1]
    if is_palindrome(encoded):
        return (encoded, True)
    else:
        decoded = ''
        i = 0
        while i < len(encoded):
            if i % 3 == 0 and i + 2 < len(encoded):
                decoded += encoded[i + 2]
                decoded += encoded[i:i + 2]
            else:
                decoded += encoded[i]
            i += 1
        return (decoded, False)