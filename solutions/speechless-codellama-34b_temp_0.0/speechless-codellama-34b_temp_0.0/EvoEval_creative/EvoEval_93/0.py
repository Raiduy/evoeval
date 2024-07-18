def secret_code(message, n_values):
    result = ''
    for (i, char) in enumerate(message):
        if char.isalpha():
            n = n_values[i % len(n_values)]
            new_char = chr((ord(char.lower()) - 96 + n) % 26 + 97)
            if char.isupper():
                new_char = new_char.upper()
            result += new_char
        else:
            result += char
    return result