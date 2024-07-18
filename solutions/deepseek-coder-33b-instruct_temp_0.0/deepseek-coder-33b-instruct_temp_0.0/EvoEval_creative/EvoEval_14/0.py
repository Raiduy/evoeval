def create_alias(name: str) -> str:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    alias = ''
    for char in name:
        if char.lower() in vowels:
            index = (vowels.index(char.lower()) + 1) % len(vowels)
            new_char = vowels[index]
            if char.isupper():
                new_char = new_char.upper()
            alias += new_char
        elif char.lower() in consonants:
            index = (consonants.index(char.lower()) + 1) % len(consonants)
            new_char = consonants[index]
            if char.isupper():
                new_char = new_char.upper()
            alias += new_char
        else:
            alias += char
    return alias