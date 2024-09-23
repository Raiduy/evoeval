
def select_words(s, n):
    vowels = 'aeiou'
    words = s.split()
    result = []
    for word in words:
        consonants = [char for char in word.lower() if char not in vowels]
        if len(consonants) == n:
            result.append(word)
    return result