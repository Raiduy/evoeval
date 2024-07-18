
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            if char.islower():
                encoded_message += chr(ord(char) + 2)
            else:
                encoded_message += chr(ord(char) - 2)
        else:
            encoded_message += char.swapcase()
    return encoded_message