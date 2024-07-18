def encode_complex(message, shift, key):
    """
    Encodes a message by swapping case, shifting vowels, and replacing consonants with key characters.
    """
    vowels = 'aeiouAEIOU'
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = ''
    for char in message:
        swapped_char = char.swapcase()
        if swapped_char.lower() in vowels:
            original_index = alphabet.index(swapped_char.lower())
            shifted_index = (original_index + shift) % 26
            new_char = alphabet[shifted_index]
            if swapped_char.isupper():
                new_char = new_char.upper()
            encoded_message += new_char
        elif swapped_char.isalpha():
            original_index = alphabet.index(swapped_char.lower())
            new_char = key[original_index]
            if swapped_char.isupper():
                new_char = new_char.upper()
            encoded_message += new_char
        else:
            encoded_message += swapped_char
    return encoded_message