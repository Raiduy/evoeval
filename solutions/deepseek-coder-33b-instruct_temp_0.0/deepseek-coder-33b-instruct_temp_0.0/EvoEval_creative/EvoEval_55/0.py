def treasure_map(message, shift):
    encrypted_message = ''
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            encrypted_message += chr((ord(char) - ascii_offset + shift + i) % 26 + ascii_offset)
        else:
            encrypted_message += char
    return encrypted_message