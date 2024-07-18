
def select_words(s, n):
    if s == '':
        return []
    else:
        words = s.split()
        selected_words = []
        for word in words:
            consonants = 0
            for letter in word:
                if letter.lower() not in 'aeiou':
                    consonants += 1
            if consonants == n:
                selected_words.append(word)
        return selected_words