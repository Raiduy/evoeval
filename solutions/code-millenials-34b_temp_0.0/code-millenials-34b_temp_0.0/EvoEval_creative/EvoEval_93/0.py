def secret_code(message, n_values):
    encoded_message = ''
    n_len = len(n_values)
    for i in range(len(message)):
        if message[i].isalpha():
            is_upper = message[i].isupper()
            message_char = ord(message[i].lower())
            n_index = i % n_len
            shift = n_values[n_index]
            new_char = chr((message_char - 97 + shift) % 26 + 97)
            if is_upper:
                encoded_message += new_char.upper()
            else:
                encoded_message += new_char
        else:
            encoded_message += message[i]
    return encoded_message