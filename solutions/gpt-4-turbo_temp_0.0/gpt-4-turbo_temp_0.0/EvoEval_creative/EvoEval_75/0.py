def magical_string_transformer(input_str):
    vowels = 'aeiou'
    consonants = ''.join([chr(i) for i in range(97, 123) if chr(i) not in vowels])
    transformed_str = ''
    for (i, char) in enumerate(input_str):
        if char.lower() in vowels:
            new_char = vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
            transformed_str += new_char.upper() if char.isupper() else new_char
        elif char.lower() in consonants:
            new_char = consonants[(consonants.index(char.lower()) + 1) % len(consonants)]
            transformed_str += new_char.upper() if char.isupper() else new_char
        elif char.isdigit():
            transformed_str += str((int(char) + 1) % 10)
        elif char in '?!':
            if i % 2 == 0:
                transformed_str += '!' if char == '?' else '?'
            else:
                transformed_str += '?' if char == '?' else '!'
        else:
            transformed_str += char
    return transformed_str