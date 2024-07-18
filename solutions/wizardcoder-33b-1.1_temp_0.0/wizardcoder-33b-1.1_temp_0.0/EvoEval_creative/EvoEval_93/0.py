def secret_code(message, n_values):
    result = ''
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + n_values[i % len(n_values)]) % 26 + ascii_offset)
        else:
            result += char
    return result