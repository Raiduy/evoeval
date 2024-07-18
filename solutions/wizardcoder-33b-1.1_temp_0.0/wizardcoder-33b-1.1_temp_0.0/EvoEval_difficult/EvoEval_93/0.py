def encode_complex(message, shift, key):
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encoded_message = ''
    for char in message:
        if char in vowels:
            if char.islower():
                encoded_message += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            else:
                encoded_message += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        elif char.isalpha():
            if char.islower():
                encoded_message += key[ord(char) - ord('a')]
            else:
                encoded_message += key[ord(char) - ord('A')]
        else:
            encoded_message += char
    return encoded_message.swapcase()