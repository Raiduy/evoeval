
def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                encoded_char = chr((ord(char.lower()) - ord('a') + 2) % 26 + ord('a'))
                if char.isupper():
                    encoded_char = encoded_char.upper()
            else:
                encoded_char = char.swapcase()
        else:
            encoded_char = char
        encoded_message += encoded_char
    return encoded_message