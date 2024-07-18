def advanced_anti_shuffle(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        ascii_sorted_word = ''.join(sorted(word, key=lambda x: ord(x)))
        shifted_word = ascii_sorted_word[n:] + ascii_sorted_word[:n]
        result.append(shifted_word)
    return ' '.join(result)