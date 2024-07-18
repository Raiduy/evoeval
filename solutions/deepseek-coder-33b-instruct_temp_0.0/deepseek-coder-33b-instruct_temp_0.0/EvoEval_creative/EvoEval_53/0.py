def magical_transformation(s):
    vowels = 'aeiou'
    vowels_upper = vowels.upper()
    consonants = 'bcdfghjklmnpqrstvwxyz'
    consonants_upper = consonants.upper()
    transformed_s = ''
    for (i, char) in enumerate(s):
        if char in vowels:
            index = vowels.index(char)
            transformed_s += vowels[(index + 1) % len(vowels)]
        elif char in vowels_upper:
            index = vowels_upper.index(char)
            transformed_s += vowels_upper[(index + 1) % len(vowels_upper)]
        elif char in consonants:
            index = consonants.index(char)
            transformed_s += consonants[(index + 1) % len(consonants)]
        elif char in consonants_upper:
            index = consonants_upper.index(char)
            transformed_s += consonants_upper[(index + 1) % len(consonants_upper)]
        elif char == '?':
            if i % 2 == 0:
                transformed_s += '!'
            else:
                transformed_s += '?'
        else:
            transformed_s += char
    return transformed_s