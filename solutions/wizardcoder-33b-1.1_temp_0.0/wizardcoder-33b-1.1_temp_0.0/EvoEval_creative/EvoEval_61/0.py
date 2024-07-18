def transform_string(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    next_vowel = {vowels[i]: vowels[(i + 1) % len(vowels)] for i in range(len(vowels))}
    prev_consonant = {consonants[i]: consonants[i - 1] for i in range(len(consonants))}
    result = []
    for (i, c) in enumerate(s):
        if c.isalpha():
            if i % 2 == 0:
                c = c.swapcase()
            if c.lower() in vowels:
                c = next_vowel[c.lower()] if c.islower() else next_vowel[c.lower()].upper()
            else:
                c = prev_consonant[c.lower()] if c.islower() else prev_consonant[c.lower()].upper()
        result.append(c)
    return ''.join(result)