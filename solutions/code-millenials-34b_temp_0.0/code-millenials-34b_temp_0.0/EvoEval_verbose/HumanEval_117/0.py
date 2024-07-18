
def select_words(s, n):
    vowels = ['a', 'e', 'i', 'o', 'u']
    words = s.split()
    selected_words = []
    for word in words:
        consonants = [letter for letter in word if letter.lower() not in vowels]
        if len(consonants) == n:
            selected_words.append(word)
    return selected_words