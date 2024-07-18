
def select_words(s, n):
    vowels = 'aeiou'
    words = s.split()
    selected_words = []
    for word in words:
        consonant_count = 0
        for char in word.lower():
            if char not in vowels:
                consonant_count += 1
        if consonant_count == n:
            selected_words.append(word)
    return selected_words