def treasure_map(message, shift):
    result = ''
    for i in range(len(message)):
        char = message[i]
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            result += chr((ord(char) - ascii_offset + i + shift) % 26 + ascii_offset)
        else:
            result += char
    return result