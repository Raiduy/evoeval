def transform_string(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    transformed = ''
    for (i, char) in enumerate(s):
        if char.lower() in vowels:
            next_vowel = vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
            transformed += next_vowel.upper() if char.isupper() else next_vowel
        elif char.lower() in consonants:
            prev_consonant = consonants[(consonants.index(char.lower()) - 1) % len(consonants)]
            if i % 2 == 1:
                transformed += prev_consonant.upper() if char.isupper() else prev_consonant
            else:
                transformed += char
        else:
            transformed += char
    return transformed