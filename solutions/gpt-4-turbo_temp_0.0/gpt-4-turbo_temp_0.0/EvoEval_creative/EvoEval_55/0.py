def treasure_map(message, shift):
    encrypted_message = ''
    for (i, char) in enumerate(message):
        current_shift = shift + i
        if char.isupper():
            encrypted_char = chr((ord(char) - ord('A') + current_shift) % 26 + ord('A'))
        elif char.islower():
            encrypted_char = chr((ord(char) - ord('a') + current_shift) % 26 + ord('a'))
        else:
            encrypted_char = char
        encrypted_message += encrypted_char
    return encrypted_message