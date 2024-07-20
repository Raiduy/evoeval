def advanced_anti_shuffle(s, n):

    def shift_word(word, n):
        return word[-n:] + word[:-n]

    def sort_word(word):
        letters = sorted([c for c in word if c.isalpha()])
        non_letters = [c for c in word if not c.isalpha()]
        return ''.join(letters + non_letters)
    words = s.split(' ')
    words = [shift_word(sort_word(word), n) for word in words]
    return ' '.join(words)