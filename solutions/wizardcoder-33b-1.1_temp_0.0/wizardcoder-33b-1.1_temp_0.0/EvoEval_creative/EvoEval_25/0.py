def word_frequency_analysis(text: str, word: str):
    sentences = text.split('. ')
    max_count = 0
    max_sentence = ''
    total_count = 0
    for sentence in sentences:
        count = sentence.lower().split().count(word.lower())
        total_count += count
        if count > max_count:
            max_count = count
            max_sentence = sentence
    return (total_count, max_sentence)