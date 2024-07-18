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
    import re

    def split_sentences(text):
        return [sentence.split() for sentence in re.split('[.!?]', text) if sentence]
    sentences = split_sentences(S)
    count = 0
    for sentence in sentences:
        if sentence[-1].lower() == 'happy':
            count += 1
    return count