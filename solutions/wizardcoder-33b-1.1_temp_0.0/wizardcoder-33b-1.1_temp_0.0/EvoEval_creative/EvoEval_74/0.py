def cipher_mapping(s, cipher):
    return ''.join([cipher[c] if c in cipher else c for c in s])