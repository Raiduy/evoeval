def create_alias(name: str) -> str:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    alias = ''
    for char in name:
        if char.isalpha():
            if char.lower() in vowels:
                index = vowels.index(char.lower())
                alias += vowels[(index + 1) % len(vowels)].upper() if char.isupper() else vowels[(index + 1) % len(vowels)].lower()
            else:
                index = consonants.index(char.lower())
                alias += consonants[(index + 1) % len(consonants)].upper() if char.isupper() else consonants[(index + 1) % len(consonants)].lower()
    return alias