
def get_closest_vowel(word):
    vowels = 'AEIOUaeiou'
    candidate_vowels = []
    for i in range(1, len(word) - 1):
        if word[i] in vowels and word[i - 1] not in vowels and (word[i + 1] not in vowels):
            candidate_vowels.append(word[i])
    if not candidate_vowels:
        return ''
    else:
        return candidate_vowels[-1]