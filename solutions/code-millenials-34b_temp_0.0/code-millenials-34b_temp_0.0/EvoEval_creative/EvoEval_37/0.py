def string_transform(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    result = ''
    for char in s:
        if char.isalpha():
            if char.lower() in vowels:
                index = vowels.index(char.lower())
                result += vowels[(index + 1) % len(vowels)].upper() if char.isupper() else vowels[(index + 1) % len(vowels)]
            else:
                index = consonants.index(char.lower())
                result += consonants[(index + 1) % len(consonants)].upper() if char.isupper() else consonants[(index + 1) % len(consonants)]
        else:
            result += char
    return result