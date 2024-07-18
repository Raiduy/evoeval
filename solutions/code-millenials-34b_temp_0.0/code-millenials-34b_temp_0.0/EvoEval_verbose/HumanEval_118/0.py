
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    candidate_vowels = []
    for i in range(len(word) - 2, -1, -1):
        if word[i] in vowels and word[i + 1] not in vowels and (word[i + 2] not in vowels):
            candidate_vowels.append(word[i])
    if candidate_vowels:
        return candidate_vowels[0]
    else:
        return ''