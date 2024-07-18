def magical_transformation(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    VOWELS = vowels.upper()
    CONSONANTS = consonants.upper()
    transformed = ''
    for (i, c) in enumerate(s):
        if c in vowels:
            transformed += vowels[(vowels.index(c) + 1) % len(vowels)]
        elif c in consonants:
            transformed += consonants[(consonants.index(c) + 1) % len(consonants)]
        elif c == 'y':
            transformed += 'z'
        elif c == 'z':
            transformed += 'b'
        elif c == '?':
            if i % 2 == 0:
                transformed += '!'
            else:
                transformed += '?'
        else:
            transformed += c
    return transformed