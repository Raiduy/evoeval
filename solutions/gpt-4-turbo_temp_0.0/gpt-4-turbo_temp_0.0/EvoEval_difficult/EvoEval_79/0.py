def decimal_to_binary(decimal, padding_length):
    if not isinstance(decimal, int) or not isinstance(padding_length, int) or decimal < 0 or (padding_length < 0):
        return 'Invalid Input'
    binary_str = bin(decimal)[2:]
    if len(binary_str) > padding_length:
        return 'Padding length is too small'
    padded_binary = binary_str.rjust(padding_length, '0')
    formatted_binary = f'db{padded_binary}db'
    return formatted_binary