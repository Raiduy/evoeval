def encode_complex(message, shift, key):
    encoded_message = ''
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                index = (alphabet.index(char.lower()) + shift) % 26
                new_char = alphabet[index]
                if char.isupper():
                    new_char = new_char.upper()
            else:
                index = key.index(char.lower())
                new_char = key[index]
                if char.isupper():
                    new_char = new_char.upper()
            encoded_message += new_char
        else:
            encoded_message += char
    return encoded_message