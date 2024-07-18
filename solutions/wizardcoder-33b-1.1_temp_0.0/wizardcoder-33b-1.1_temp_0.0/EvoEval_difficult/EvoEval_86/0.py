def advanced_anti_shuffle(s, n):
    words = s.split(' ')
    result = []
    for word in words:
        punctuation = ''
        while not word[-1].isalpha():
            punctuation = word[-1] + punctuation
            word = word[:-1]
        word = ''.join(sorted(word))
        word = word[-n:] + word[:-n]
        result.append(word + punctuation)
    return ' '.join(result)