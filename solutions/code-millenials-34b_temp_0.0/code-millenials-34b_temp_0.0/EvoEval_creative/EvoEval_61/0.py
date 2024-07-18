def transform_string(s):
    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'
    new_s = ''
    for i in range(len(s)):
        if s[i] == ' ':
            new_s += ' '
        else:
            if i % 2 != 0:
                new_s += s[i].swapcase()
            else:
                new_s += s[i]
            if new_s[-1].lower() in vowels:
                new_s = new_s[:-1] + vowels[(vowels.index(new_s[-1].lower()) + 1) % len(vowels)]
            elif new_s[-1].lower() in consonants:
                new_s = new_s[:-1] + consonants[(consonants.index(new_s[-1].lower()) - 1) % len(consonants)]
    return new_s