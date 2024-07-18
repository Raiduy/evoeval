def cipher_mapping(s, cipher):
    new_s = ''
    for char in s:
        if char in cipher:
            new_s += cipher[char]
        else:
            new_s += char
    return new_s