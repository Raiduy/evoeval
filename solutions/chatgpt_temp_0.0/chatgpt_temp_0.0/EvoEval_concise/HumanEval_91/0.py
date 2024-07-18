
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
    sentences = S.split('. ') + S.split('? ') + S.split('! ')
    count = 0
    for sentence in sentences:
        if sentence.startswith('I'):
            count += 1
    return count