def decimal_to_binary(decimal, padding_length):
    if not isinstance(decimal, int) or not isinstance(padding_length, int):
        return 'Invalid Input'
    if decimal < 0 or padding_length < 0:
        return 'Invalid Input'
    binary = bin(decimal)[2:]
    if len(binary) > padding_length:
        return 'Padding length is too small'
    padded_binary = binary.zfill(padding_length)
    return f'db{padded_binary}db'