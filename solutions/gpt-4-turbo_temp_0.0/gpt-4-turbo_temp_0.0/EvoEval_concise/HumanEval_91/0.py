
def is_bored(S):
    """
    Given a string of sentences, this function counts the number of sentences starting with "I". 
    Sentences are separated by '.', '?' or '!'.
    
    Example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    sentences = []
    temp_sentence = ''
    for char in S:
        if char in '.?!':
            if temp_sentence:
                sentences.append(temp_sentence.strip())
                temp_sentence = ''
        else:
            temp_sentence += char
    if temp_sentence:
        sentences.append(temp_sentence.strip())
    count = 0
    for sentence in sentences:
        if sentence.startswith('I '):
            count += 1
    return count