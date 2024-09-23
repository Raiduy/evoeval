def magical_string_transformer(input_str):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    digits = '0123456789'
    special_chars = {'?': '!', '!': '?'}
    transformed_str = ''
    for (i, char) in enumerate(input_str):
        if char.lower() in vowels:
            transformed_str += vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
            if char.isupper():
                transformed_str = transformed_str[:-1] + transformed_str[-1].upper()
        elif char.lower() in consonants:
            transformed_str += consonants[(consonants.index(char.lower()) + 1) % len(consonants)]
            if char.isupper():
                transformed_str = transformed_str[:-1] + transformed_str[-1].upper()
        elif char in digits:
            transformed_str += digits[(digits.index(char) + 1) % len(digits)]
        elif char in special_chars.keys():
            if i % 2 == 0:
                transformed_str += special_chars[char]
            else:
                transformed_str += char
        else:
            transformed_str += char
    return transformed_str