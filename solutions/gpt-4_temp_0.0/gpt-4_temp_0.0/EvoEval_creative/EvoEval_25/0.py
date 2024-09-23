def word_frequency_analysis(text: str, word: str):
    sentences = text.split('.')
    word_frequency = text.lower().count(word.lower())
    max_frequency_sentence = ''
    max_frequency = 0
    for sentence in sentences:
        sentence_frequency = sentence.lower().count(word.lower())
        if sentence_frequency > max_frequency:
            max_frequency = sentence_frequency
            max_frequency_sentence = sentence.strip()
    return (word_frequency, max_frequency_sentence if max_frequency > 0 else '')