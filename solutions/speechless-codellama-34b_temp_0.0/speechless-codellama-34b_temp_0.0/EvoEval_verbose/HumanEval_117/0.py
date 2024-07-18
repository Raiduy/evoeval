
def select_words(s, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = s.split()
    output = []
    for word in words:
        consonants = 0
        for letter in word:
            if letter.lower() not in vowels:
                consonants += 1
        if consonants == n:
            output.append(word)
    return output