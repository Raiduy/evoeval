def magical_string_transformer(input_str):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    digits = '0123456789'
    output_str = ''
    for (i, char) in enumerate(input_str):
        if char in vowels:
            output_str += vowels[(vowels.index(char) + 1) % len(vowels)]
        elif char in consonants:
            output_str += consonants[(consonants.index(char) + 1) % len(consonants)]
        elif char in digits:
            output_str += str((int(char) + 1) % 10)
        elif char == '?':
            if i % 2 == 0:
                output_str += '!'
            else:
                output_str += '?'
        else:
            output_str += char
    return output_str