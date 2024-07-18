def secret_code(message, n_values):
    result = ''
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            shift = n_values[i % len(n_values)]
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result