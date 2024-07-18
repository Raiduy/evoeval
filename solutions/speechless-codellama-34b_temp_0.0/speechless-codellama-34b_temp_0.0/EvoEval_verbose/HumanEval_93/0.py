
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            encoded_message += chr((ord(char) - ord('a') + 2) % 26 + ord('a'))
        else:
            encoded_message += char.swapcase()
    return encoded_message