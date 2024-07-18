def string_transform(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    transformed = ''
    for char in s:
        if char.isalpha():
            if char.lower() in vowels:
                transformed += vowels[(vowels.index(char.lower()) + 1) % len(vowels)].upper() if char.isupper() else vowels[(vowels.index(char.lower()) + 1) % len(vowels)].lower()
            elif char.lower() in consonants:
                transformed += consonants[(consonants.index(char.lower()) + 1) % len(consonants)].upper() if char.isupper() else consonants[(consonants.index(char.lower()) + 1) % len(consonants)].lower()
        else:
            transformed += char
    return transformed