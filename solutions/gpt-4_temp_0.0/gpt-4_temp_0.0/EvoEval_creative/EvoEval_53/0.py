def magical_transformation(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    transformed = ''
    for (i, char) in enumerate(s):
        if char.lower() in vowels:
            next_vowel = vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
            transformed += next_vowel.upper() if char.isupper() else next_vowel
        elif char.lower() in consonants:
            next_consonant = consonants[(consonants.index(char.lower()) + 1) % len(consonants)]
            transformed += next_consonant.upper() if char.isupper() else next_consonant
        elif char in ['?', '!']:
            transformed += '!' if i % 2 == 0 else '?'
        else:
            transformed += char
    return transformed