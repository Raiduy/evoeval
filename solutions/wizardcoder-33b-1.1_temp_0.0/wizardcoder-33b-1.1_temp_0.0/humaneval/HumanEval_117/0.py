
def select_words(s, n):
    vowels = 'aeiou'
    words = s.split()
    result = []
    for word in words:
        count = sum(1 for char in word if char.lower() not in vowels)
        if count == n:
            result.append(word)
    return result
