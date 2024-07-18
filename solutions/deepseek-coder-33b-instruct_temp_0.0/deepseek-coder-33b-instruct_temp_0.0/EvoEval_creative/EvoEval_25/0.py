def word_frequency_analysis(text: str, word: str):
    """Return the frequency of the given word in a text. Also, return the sentence in which the word appears the most times.

    The function will return a tuple where the first element is the frequency of the word, and the second element is the sentence with the max frequency of the word. If the word is not found in the text, return (0, ""). 

    Assume that sentences end with a period.

    >>> word_frequency_analysis("Hello world. I love this world.", "world")
    (2, "Hello world")

    >>> word_frequency_analysis("This is the best day. I love this day because it's sunny.", "day")
    (2, "This is the best day")

    >>> word_frequency_analysis("This is a test. Testing is fun.", "test")
    (1, "This is a test")

    >>> word_frequency_analysis("Welcome to the world of coding.", "python")
    (0, "")
    """
    sentences = text.split('.')
    max_count = 0
    max_sentence = ''
    word_count = 0
    for sentence in sentences:
        words = sentence.split()
        count = words.count(word)
        if count > max_count:
            max_count = count
            max_sentence = sentence.strip()
        word_count += count
    return (word_count, max_sentence)