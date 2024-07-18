def advanced_anti_shuffle(s, n):
    words = s.split(' ')
    for (i, word) in enumerate(words):
        if word[-1].isalpha():
            punctuation = ''
        else:
            punctuation = word[-1]
            word = word[:-1]
        sorted_word = ''.join(sorted(word))
        if len(sorted_word) > 0:
            n_mod = n % len(sorted_word)
            shifted_word = sorted_word[-n_mod:] + sorted_word[:-n_mod]
        else:
            shifted_word = sorted_word
        words[i] = shifted_word + punctuation
    return ' '.join(words)