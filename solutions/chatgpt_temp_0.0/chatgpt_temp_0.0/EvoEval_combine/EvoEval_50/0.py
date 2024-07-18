
def get_closest_upper_vowel(word):
    vowels = set('AEIOU')
    word = word[::-1]
    for (i, char) in enumerate(word):
        if char.isupper() and char in vowels and (i % 2 == 0):
            if i > 0 and i < len(word) - 1 and word[i - 1].isalpha() and word[i + 1].isalpha():
                return char
    return ''