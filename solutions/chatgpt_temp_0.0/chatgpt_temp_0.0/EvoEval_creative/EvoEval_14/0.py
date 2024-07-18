def create_alias(name: str) -> str:
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    alias = ''
    for char in name:
        if char.isalpha():
            if char.lower() in vowels:
                if char.isupper():
                    alias += vowels[(vowels.index(char.lower()) + 1) % len(vowels)].upper()
                else:
                    alias += vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
            elif char.isupper():
                alias += consonants[(consonants.index(char.lower()) + 1) % len(consonants)].upper()
            else:
                alias += consonants[(consonants.index(char.lower()) + 1) % len(consonants)]
        else:
            alias += char
    return alias