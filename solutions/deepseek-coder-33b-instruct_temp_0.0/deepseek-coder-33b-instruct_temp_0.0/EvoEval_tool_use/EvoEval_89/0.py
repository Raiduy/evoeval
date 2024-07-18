def split_sentences(text):
    """
    Given a text, it splits it into sentences. Sentences are delimited by '.', '?' or '!'.
    This function returns a list of sentences where each sentence is a list of words.

    For example:
    >>> split_sentences("Hello world. How are you?")
    [["Hello", "world"], ["How", "are", "you"]]
    """
    import re

    return [sentence.split() for sentence in re.split("[.!?]", text) if sentence]
def is_happy(S):
    """
    You'll be given a string of words, and your task is to count the number
    of happy moments. A happy moment is a sentence that ends with the word "happy".
    Sentences are delimited by '.', '?' or '!'

    For example:
    >>> is_happy("Hello world. I am happy")
    1
    >>> is_happy("The sky is blue. The sun is shining.")
    0
    """
    sentences = split_sentences(S)
    happy_count = 0
    for sentence in sentences:
        if sentence[-1].lower() == 'happy':
            happy_count += 1
    return happy_count