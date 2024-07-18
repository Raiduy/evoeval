
def encode(message):
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = (vowels.index(char.lower()) + 2) % 5
                encoded_char = vowels[index].upper() if char.isupper() else vowels[index]
            else:
                encoded_char = char.lower() if char.isupper() else char.upper()
            encoded_message += encoded_char
        else:
            encoded_message += char
    return encoded_message
