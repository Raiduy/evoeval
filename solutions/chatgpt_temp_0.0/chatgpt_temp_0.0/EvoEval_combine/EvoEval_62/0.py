
def strange_word_sort(text):
    words = text.split()
    words = [word.lower() for word in words]
    words.sort(key=lambda x: (x.lower(), -len(x)))
    sorted_text = '-'.join(words)
    sorted_text = sorted_text.replace('  ', '-')
    sorted_text = sorted_text.replace(' ', '_')
    return sorted_text