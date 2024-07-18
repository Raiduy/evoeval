def advanced_anti_shuffle(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        sorted_word = ''.join(sorted(word))
        shifted_word = sorted_word[-n:] + sorted_word[:-n]
        result.append(shifted_word)
    return ' '.join(result)