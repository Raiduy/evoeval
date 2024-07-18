
def strange_word_sort(text):
    text = text.replace(' ' * 2, '-')
    text = text.replace(' ', '_')
    words = text.split('_')
    strange_order = sorted(words, key=lambda x: (len(x) % 2, x))
    result = ' '.join(strange_order)
    result = result.replace('-', ' ' * 2).replace('_', ' ')
    return result