def transform_string(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyza'
    transformed_string = ''
    for (i, char) in enumerate(s):
        if char.isalpha():
            if i % 2 == 1:
                if char.lower() in vowels:
                    transformed_string += vowels[(vowels.index(char.lower()) + 1) % len(vowels)]
                else:
                    transformed_string += consonants[(consonants.index(char.lower()) - 1) % len(consonants)]
            else:
                transformed_string += char
        else:
            transformed_string += char
    return transformed_string