
def get_closest_vowel(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    consonants = [c for c in word if c.isalpha() and c.lower() not in vowels]
    if len(consonants) < 2:
        return ''
    for i in range(len(consonants) - 2, -1, -1):
        if consonants[i].lower() in vowels:
            return consonants[i]
    return ''