
def find_max(words):
    max_word = ''
    max_unique_chars = 0
    words.sort()
    for word in words:
        unique_chars = len(set(word))
        if unique_chars > max_unique_chars:
            max_word = word
            max_unique_chars = unique_chars
    return max_word