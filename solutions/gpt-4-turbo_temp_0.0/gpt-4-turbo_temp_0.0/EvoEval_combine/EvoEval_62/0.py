
def strange_word_sort(text):
    text = text.replace('   ', '-')
    text = text.replace(' ', '_')
    words = []
    temp_word = ''
    for char in text:
        if char in '-_':
            if temp_word:
                words.append(temp_word)
                temp_word = ''
            words.append(char)
        else:
            temp_word += char
    if temp_word:
        words.append(temp_word)
    words = [word for word in words if word not in '-_']
    words.sort(key=str.lower)
    strange_sorted_words = []
    while words:
        if words:
            strange_sorted_words.append(words.pop(0))
        if words:
            strange_sorted_words.append(words.pop(-1))
    result = []
    for word in strange_sorted_words:
        if result and result[-1] not in '-_':
            result.append('_')
        result.append(word)
    final_result = ''.join(result).replace('_-', '-').replace('-_', '-')
    return final_result