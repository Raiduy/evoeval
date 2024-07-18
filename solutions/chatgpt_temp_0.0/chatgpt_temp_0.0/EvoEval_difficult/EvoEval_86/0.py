def advanced_anti_shuffle(s, n):
    words = s.split()
    ordered_words = []
    for word in words:
        sorted_word = ''.join(sorted(word, key=lambda x: ord(x)))
        shifted_word = sorted_word[-n:] + sorted_word[:-n]
        ordered_words.append(shifted_word)
    return ' '.join(ordered_words)