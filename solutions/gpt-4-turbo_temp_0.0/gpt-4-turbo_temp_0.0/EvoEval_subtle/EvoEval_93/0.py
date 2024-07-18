

def encode(message):
    vowel_replacement = {'a': 'd', 'e': 'h', 'i': 'l', 'o': 'r', 'u': 'x', 'A': 'D', 'E': 'H', 'I': 'L', 'O': 'R', 'U': 'X'}
    encoded_message = ''
    for char in message:
        if char in vowel_replacement:
            encoded_message += vowel_replacement[char]
        elif char.islower():
            encoded_message += char.upper()
        else:
            encoded_message += char.lower()
    return encoded_message