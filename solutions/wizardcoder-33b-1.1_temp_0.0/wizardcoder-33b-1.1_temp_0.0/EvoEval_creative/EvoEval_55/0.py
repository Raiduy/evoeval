def treasure_map(message, shift):
    cipher = ''
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            cipher += chr((ord(char) - ascii_offset + shift + i) % 26 + ascii_offset)
        else:
            cipher += char
    return cipher