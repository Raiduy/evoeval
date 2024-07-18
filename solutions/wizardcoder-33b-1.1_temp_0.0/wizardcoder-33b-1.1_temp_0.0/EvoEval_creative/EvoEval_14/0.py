def create_alias(name: str) -> str:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    alias = ''
    for char in name:
        if char.lower() in vowels:
            index = vowels.index(char.lower())
            new_char = vowels[(index + 1) % len(vowels)]
            alias += new_char if char.islower() else new_char.upper()
        elif char.lower() in consonants:
            index = consonants.index(char.lower())
            new_char = consonants[(index + 1) % len(consonants)]
            alias += new_char if char.islower() else new_char.upper()
        else:
            alias += char
    return alias