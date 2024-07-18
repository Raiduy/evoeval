def transform_string(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    s = list(s)
    for i in range(len(s)):
        if i % 2 != 0 and s[i].isalpha():
            s[i] = s[i].swapcase()
        if s[i].lower() in vowels:
            s[i] = vowels[(vowels.index(s[i].lower()) + 1) % 5]
            if s[i].isupper():
                s[i] = s[i].upper()
        elif s[i].lower() in consonants:
            s[i] = consonants[(consonants.index(s[i].lower()) - 1) % 21]
            if s[i].isupper():
                s[i] = s[i].upper()
    return ''.join(s)