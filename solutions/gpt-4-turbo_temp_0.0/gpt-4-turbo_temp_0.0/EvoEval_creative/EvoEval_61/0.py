def transform_string(s):

    def swap_case(c):
        return c.lower() if c.isupper() else c.upper()

    def next_vowel(v):
        vowels = 'aeiou'
        return vowels[(vowels.index(v.lower()) + 1) % len(vowels)]

    def preceding_consonant(c):
        consonants = 'bcdfghjklmnpqrstvwxyz'
        index = consonants.index(c.lower()) - 1
        return consonants[index]
    result = []
    for (i, char) in enumerate(s):
        if char.isalpha():
            if i % 2 == 1:
                char = swap_case(char)
            if char.lower() in 'aeiou':
                char = next_vowel(char)
                if s[i].isupper():
                    char = char.upper()
            else:
                char = preceding_consonant(char)
                if s[i].isupper():
                    char = char.upper()
        result.append(char)
    return ''.join(result)