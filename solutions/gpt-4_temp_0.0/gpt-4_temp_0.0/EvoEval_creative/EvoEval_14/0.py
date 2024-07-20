def create_alias(name: str) -> str:
    """ For a given name, create an alias following these rules:
        If the name includes a vowel, replace it with the next vowel in the cycle a->e->i->o->u->a. 
        If the name includes a consonant, replace it with the next consonant in alphabetical order, once 'z' is reached, loop back to 'b'.
        The alias should maintain the original names case (upper or lower)
        Ignore any non-alphabetical characters.

    >>> create_alias('John Doe')
    'Kujp Fui'
    """
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    alias = ''
    for char in name:
        if char.lower() in vowels:
            next_vowel = vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
            alias += next_vowel.upper() if char.isupper() else next_vowel
        elif char.lower() in consonants:
            next_consonant = consonants[(consonants.index(char.lower()) + 1) % len(consonants)]
            alias += next_consonant.upper() if char.isupper() else next_consonant
        else:
            alias += char
    return alias