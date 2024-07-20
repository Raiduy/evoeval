def encode_complex(message, shift, key):
    vowels = 'aeiou'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                new_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
                encoded_message += new_char.upper() if char.isupper() else new_char
            else:
                new_char = key[alphabet.index(char.lower())]
                encoded_message += new_char.upper() if char.isupper() else new_char
        else:
            encoded_message += char
    return encoded_message