def word_frequency_analysis(text: str, word: str):
    sentences = text.split('. ')
    max_freq = 0
    max_sentence = ''
    for sentence in sentences:
        freq = sentence.count(word)
        if freq > max_freq:
            max_freq = freq
            max_sentence = sentence
    return (max_freq, max_sentence) if max_freq > 0 else (0, '')