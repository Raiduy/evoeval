def encode_complex(message, shift, key):
    vowels = 'aeiou'
    encoded_message = ''
    for char in message:
        if char.isalpha():
            if char.lower() in vowels:
                vowel_index = ord(char.lower()) - ord('a')
                encoded_char = key[(vowel_index + shift) % 26]
                if char.isupper():
                    encoded_message += encoded_char.upper()
                else:
                    encoded_message += encoded_char.lower()
            else:
                consonant_index = ord(char.lower()) - ord('a')
                encoded_char = key[consonant_index]
                if char.isupper():
                    encoded_message += encoded_char.upper()
                else:
                    encoded_message += encoded_char.lower()
        else:
            encoded_message += char
    return encoded_message