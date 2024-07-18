
def find_max(words):
    max_unique_count = -1
    max_word = ''
    for word in words:
        unique_chars = set(word)
        unique_count = len(unique_chars)
        if unique_count > max_unique_count or (unique_count == max_unique_count and word < max_word):
            max_unique_count = unique_count
            max_word = word
    return max_word