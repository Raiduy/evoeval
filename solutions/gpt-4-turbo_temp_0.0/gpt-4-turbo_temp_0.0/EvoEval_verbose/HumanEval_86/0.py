
def anti_shuffle(s):
    words = s.split(' ')
    sorted_words = []
    for word in words:
        chars = [c for c in word if c.isalpha()]
        non_chars = [(i, c) for (i, c) in enumerate(word) if not c.isalpha()]
        sorted_chars = sorted(chars)
        for (i, c) in non_chars:
            sorted_chars.insert(i, c)
        sorted_word = ''.join(sorted_chars)
        sorted_words.append(sorted_word)
    return ' '.join(sorted_words)