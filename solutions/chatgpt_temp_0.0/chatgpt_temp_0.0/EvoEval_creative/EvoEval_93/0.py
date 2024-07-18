def secret_code(message, n_values):
    encoded_message = ''
    n_values_cycle = cycle(n_values)
    for char in message:
        if char.isalpha():
            n = next(n_values_cycle)
            if char.isupper():
                encoded_char = chr((ord(char) - 65 + n) % 26 + 65)
            else:
                encoded_char = chr((ord(char) - 97 + n) % 26 + 97)
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message