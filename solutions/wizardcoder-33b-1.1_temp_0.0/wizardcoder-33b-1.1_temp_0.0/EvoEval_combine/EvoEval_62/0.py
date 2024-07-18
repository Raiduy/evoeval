
def strange_word_sort(text):
    text = text.replace('   ', '-')
    text = text.replace(' ', '_')
    words = text.split('_')
    words.sort(key=str.lower)
    sorted_words = []
    while words:
        sorted_words.append(words.pop(0))
        if words:
            sorted_words.append(words.pop())
    return '_'.join(sorted_words)