def magical_string_transformer(input_str):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    result = ''
    for (i, char) in enumerate(input_str):
        if char.lower() in vowels:
            index = (vowels.index(char.lower()) + 1) % len(vowels)
            result += vowels[index] if char.islower() else vowels[index].upper()
        elif char.lower() in consonants:
            index = (consonants.index(char.lower()) + 1) % len(consonants)
            result += consonants[index] if char.islower() else consonants[index].upper()
        elif char.isdigit():
            result += str((int(char) + 1) % 10)
        elif char in '!?':
            if i % 2 == 0:
                result += '!' if char == '?' else '?'
            else:
                result += char
        else:
            result += char
    return result