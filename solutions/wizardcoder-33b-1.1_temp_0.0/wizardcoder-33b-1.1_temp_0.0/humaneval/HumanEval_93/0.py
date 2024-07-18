
def encode(message):
    vowels = 'aeiouAEIOU'
    trans = str.maketrans(vowels, ''.join([chr((ord(c) - ord('a') + 2) % 26 + ord('a')) for c in vowels] +
                                           [chr((ord(c) - ord('A') + 2) % 26 + ord('A')) for c in vowels]))
    return message.translate(trans).swapcase()

