

def encode(message):
    vowels = 'aeiouAEIOU'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = vowels.index(char.lower())
                new_char = vowels[(index + 3) % 10]
                if char.isupper():
                    new_char = new_char.upper()
                encoded_message += new_char
            else:
                encoded_message += char.swapcase()
        else:
            encoded_message += char
    return encoded_message