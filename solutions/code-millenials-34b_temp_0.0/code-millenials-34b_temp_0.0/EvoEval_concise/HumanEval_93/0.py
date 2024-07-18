
def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char in vowels:
            if char.islower():
                encoded_message += chr(ord('a') + (ord(char) - ord('a') + 2) % 26)
            else:
                encoded_message += chr(ord('A') + (ord(char) - ord('A') + 2) % 26)
        else:
            encoded_message += char.swapcase()
    return encoded_message