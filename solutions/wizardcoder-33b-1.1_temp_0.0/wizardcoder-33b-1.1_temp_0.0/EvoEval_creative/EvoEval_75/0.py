def magical_string_transformer(input_str):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    result = ''
    for (i, char) in enumerate(input_str):
        if char.lower() in vowels:
            index = (vowels.index(char.lower()) + 1) % len(vowels)
            if char.isupper():
                result += vowels[index].upper()
            else:
                result += vowels[index]
        elif char.lower() in consonants:
            index = (consonants.index(char.lower()) + 1) % len(consonants)
            if char.isupper():
                result += consonants[index].upper()
            else:
                result += consonants[index]
        elif char.isdigit():
            result += str((int(char) + 1) % 10)
        elif char == '?':
            if i % 2 == 0:
                result += '!'
            else:
                result += '?'
        else:
            result += char
    return result