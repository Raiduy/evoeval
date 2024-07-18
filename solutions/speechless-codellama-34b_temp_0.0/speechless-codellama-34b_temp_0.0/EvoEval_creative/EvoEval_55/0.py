def treasure_map(message, shift):
    result = ''
    for (i, char) in enumerate(message):
        if char.isalpha():
            shift_amount = shift + i
            if char.islower():
                result += chr((ord(char) - 97 + shift_amount) % 26 + 97)
            else:
                result += chr((ord(char) - 65 + shift_amount) % 26 + 65)
        else:
            result += char
    return result