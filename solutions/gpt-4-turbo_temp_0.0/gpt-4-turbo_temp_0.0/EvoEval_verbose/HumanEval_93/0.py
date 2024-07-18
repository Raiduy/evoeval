
def encode(message):
    """
    This function encodes a message by swapping case of all letters and replacing vowels with the letter two places ahead.
    """
    vowel_replacement = {'a': 'c', 'e': 'g', 'i': 'k', 'o': 'q', 'u': 'w', 'A': 'C', 'E': 'G', 'I': 'K', 'O': 'Q', 'U': 'W'}
    encoded_message = []
    for char in message:
        if char in vowel_replacement:
            encoded_message.append(vowel_replacement[char])
        else:
            encoded_message.append(char.swapcase())
    return ''.join(encoded_message)