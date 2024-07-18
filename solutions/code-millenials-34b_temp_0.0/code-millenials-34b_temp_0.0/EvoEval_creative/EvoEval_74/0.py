def cipher_mapping(s, cipher):
    result = ''
    for char in s:
        if char in cipher:
            result += cipher[char]
        else:
            result += char
    return result