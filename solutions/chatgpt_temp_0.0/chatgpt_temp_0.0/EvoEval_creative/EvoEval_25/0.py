def word_frequency_analysis(text: str, word: str):
    sentences = text.split('.')
    max_frequency = 0
    max_sentence = ''
    word_count = 0
    for sentence in sentences:
        count = sentence.strip().split().count(word)
        if count > word_count:
            word_count = count
            max_sentence = sentence.strip()
    return (word_count, max_sentence)