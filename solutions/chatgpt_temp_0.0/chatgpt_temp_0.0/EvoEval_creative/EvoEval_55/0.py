def treasure_map(message, shift):

    def shift_char(char, shift):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            return chr((ord(char) - base + shift) % 26 + base)
        return char
    encrypted_message = ''
    for (i, char) in enumerate(message):
        encrypted_message += shift_char(char, shift + i)
    return encrypted_message