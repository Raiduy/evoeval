def magical_transformation(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel_dict = {vowels[i]: vowels[(i + 1) % 5] for i in range(5)}
    consonant_dict = {consonants[i]: consonants[(i + 1) % 21] for i in range(21)}
    transformed = []
    for (i, c) in enumerate(s):
        if c in vowels:
            transformed.append(vowel_dict[c])
        elif c in consonants:
            transformed.append(consonant_dict[c])
        elif c == '?' and i % 2 == 0:
            transformed.append('!')
        elif c == '!' and i % 2 == 1:
            transformed.append('?')
        else:
            transformed.append(c)
    return ''.join(transformed)