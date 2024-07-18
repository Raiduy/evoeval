def word_frequency_analysis(text: str, word: str):
    sentences = text.split('. ')
    word_count = 0
    max_count = 0
    max_sentence = ''
    for sentence in sentences:
        if word in sentence:
            count = sentence.count(word)
            word_count += count
            if count > max_count:
                max_count = count
                max_sentence = sentence
    return (word_count, max_sentence)