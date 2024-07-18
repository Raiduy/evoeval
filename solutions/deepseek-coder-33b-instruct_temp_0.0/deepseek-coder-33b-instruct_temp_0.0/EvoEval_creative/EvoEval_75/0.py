def magical_string_transformer(input_str):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    numbers = '0123456789'
    punctuation = '!@#$%^&*()-_=+[]{}|;:,.<>?`~'
    transformed_str = ''
    for (i, char) in enumerate(input_str):
        if char.lower() in vowels:
            transformed_str += vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
        elif char.lower() in consonants:
            transformed_str += consonants[(consonants.index(char.lower()) + 1) % len(consonants)]
        elif char in numbers:
            transformed_str += numbers[(numbers.index(char) + 1) % len(numbers)]
        elif char in punctuation:
            if char == '?' and i % 2 == 0:
                transformed_str += '!'
            elif char == '!' and i % 2 != 0:
                transformed_str += '?'
            else:
                transformed_str += char
        else:
            transformed_str += char
    return transformed_str