def magical_string_transformer(input_str):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    digits = '0123456789'
    punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>/?`~'
    transformed_str = ''
    for (i, char) in enumerate(input_str):
        if char.lower() in vowels:
            transformed_str += vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
        elif char.lower() in consonants:
            transformed_str += consonants[(consonants.index(char.lower()) + 1) % len(consonants)]
        elif char in digits:
            transformed_str += str((int(char) + 1) % 10)
        elif char in punctuation:
            if i % 2 == 0:
                transformed_str += char
            else:
                transformed_str += '!' if char == '?' else '?'
        else:
            transformed_str += char
    return transformed_str