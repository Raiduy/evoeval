def magical_transformation(s):
    vowels = 'aeiouAEIOU'
    consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
    vowel_map = {'a': 'e', 'e': 'i', 'i': 'o', 'o': 'u', 'u': 'a', 'A': 'E', 'E': 'I', 'I': 'O', 'O': 'U', 'U': 'A'}
    consonant_map = {consonants[i]: consonants[(i + 1) % len(consonants)] for i in range(len(consonants))}
    result = ''
    for (i, char) in enumerate(s):
        if char in vowels:
            result += vowel_map[char]
        elif char in consonants:
            result += consonant_map[char]
        elif char == '?' and i % 2 == 0:
            result += '!'
        elif char == '!' and i % 2 == 0:
            result += '?'
        else:
            result += char
    return result