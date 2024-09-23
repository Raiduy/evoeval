def secret_code(message, n_values):
    encoded_message = ''
    n_values_len = len(n_values)
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encoded_char = chr((ord(char) - ascii_offset + n_values[i % n_values_len]) % 26 + ascii_offset)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message