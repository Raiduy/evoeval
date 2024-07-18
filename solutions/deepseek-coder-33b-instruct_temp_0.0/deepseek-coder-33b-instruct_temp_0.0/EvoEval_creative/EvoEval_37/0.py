def string_transform(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    transformed_s = ''
    for char in s:
        if char.lower() in vowels:
            if char.isupper():
                transformed_s += vowels[(vowels.index(char.lower()) + 1) % len(vowels)].upper()
            else:
                transformed_s += vowels[(vowels.index(char) + 1) % len(vowels)]
        elif char.lower() in consonants:
            if char.isupper():
                transformed_s += consonants[(consonants.index(char.lower()) + 1) % len(consonants)].upper()
            else:
                transformed_s += consonants[(consonants.index(char) + 1) % len(consonants)]
        else:
            transformed_s += char
    return transformed_s