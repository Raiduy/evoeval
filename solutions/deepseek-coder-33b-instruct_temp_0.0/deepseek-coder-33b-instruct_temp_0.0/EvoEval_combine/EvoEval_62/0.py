
def strange_word_sort(text):
    if not text:
        return ''
    words = text.split()
    words.sort(key=str.lower)
    result = []
    while words:
        result.append(words.pop(0))
        if words:
            result.append(words.pop())
    result_str = ''.join(result)
    result_str = result_str.replace(' ', '_')
    result_str = result_str.replace('__', '-')
    return result_str