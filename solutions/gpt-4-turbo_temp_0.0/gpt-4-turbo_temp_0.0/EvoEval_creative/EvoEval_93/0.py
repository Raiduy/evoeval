def secret_code(message, n_values):

    def shift_char(c, n):
        if c.isalpha():
            start = ord('a') if c.islower() else ord('A')
            return chr((ord(c) - start + n) % 26 + start)
        else:
            return c
    encoded_message = ''
    n_values_len = len(n_values)
    for (i, char) in enumerate(message):
        n = n_values[i % n_values_len]
        encoded_message += shift_char(char, n)
    return encoded_message