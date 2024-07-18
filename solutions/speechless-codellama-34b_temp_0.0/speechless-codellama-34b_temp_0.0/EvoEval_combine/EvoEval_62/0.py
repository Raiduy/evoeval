
def strange_word_sort(text):
    words = text.split()
    sorted_words = []
    while words:
        min_word = min(words, key=lambda x: x.lower())
        sorted_words.append(min_word)
        words.remove(min_word)
        if words:
            max_word = max(words, key=lambda x: x.lower())
            sorted_words.append(max_word)
            words.remove(max_word)
    return '_'.join(sorted_words).replace(' ', '_').replace('--', '-')