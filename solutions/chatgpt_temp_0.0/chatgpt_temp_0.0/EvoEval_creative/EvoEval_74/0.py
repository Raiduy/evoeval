def cipher_mapping(s, cipher):
    if not s:
        return ''
    new_string = ''
    for char in s:
        if char in cipher:
            new_string += cipher[char]
        else:
            new_string += char
    return new_string