
def encode(message):
    vowels = 'aeiouAEIOU'
    trans = str.maketrans(vowels, ''.join([chr(ord(c) + 2) for c in vowels]))
    return message.translate(trans).swapcase()