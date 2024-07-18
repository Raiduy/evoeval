def create_alias(name: str) -> str:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    new_name = ''
    for char in name:
        if char.lower() in vowels:
            index = vowels.find(char.lower())
            new_char = vowels[(index + 1) % 5] if char.islower() else vowels[(index + 1) % 5].upper()
            new_name += new_char
        elif char.lower() in consonants:
            index = consonants.find(char.lower())
            new_char = consonants[(index + 1) % 21] if char.islower() else consonants[(index + 1) % 21].upper()
            new_name += new_char
        else:
            new_name += char
    return new_name