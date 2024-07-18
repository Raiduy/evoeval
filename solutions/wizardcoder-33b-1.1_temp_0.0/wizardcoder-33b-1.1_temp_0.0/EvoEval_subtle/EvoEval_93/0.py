

def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char in vowels:
                index = vowels.index(char)
                encoded_char = vowels[(index + 3) % len(vowels)]
                if char.isupper():
                    encoded_char = encoded_char.upper()
                encoded_message += encoded_char
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message