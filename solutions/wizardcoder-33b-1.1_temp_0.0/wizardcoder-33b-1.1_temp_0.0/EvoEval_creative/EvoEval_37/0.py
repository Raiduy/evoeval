def string_transform(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    vowel_map = str.maketrans(vowels, 'eioua')
    consonant_map = str.maketrans(consonants, 'bcdfghjklmnpqrstvwxyza')
    return s.translate(vowel_map).translate(consonant_map)