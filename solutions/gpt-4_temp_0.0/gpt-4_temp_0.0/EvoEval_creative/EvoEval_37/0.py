def string_transform(s):
    vowels_lower = 'aeiou'
    vowels_upper = 'AEIOU'
    consonants_lower = 'bcdfghjklmnpqrstvwxyz'
    consonants_upper = 'BCDFGHJKLMNPQRSTVWXYZ'
    transformed = ''
    for char in s:
        if char in vowels_lower:
            transformed += vowels_lower[(vowels_lower.index(char) + 1) % 5]
        elif char in vowels_upper:
            transformed += vowels_upper[(vowels_upper.index(char) + 1) % 5]
        elif char in consonants_lower:
            transformed += consonants_lower[(consonants_lower.index(char) + 1) % 21]
        elif char in consonants_upper:
            transformed += consonants_upper[(consonants_upper.index(char) + 1) % 21]
        else:
            transformed += char
    return transformed