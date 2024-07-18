
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
    sentences = [sentence.strip() for sentence in re.split('[.?!]', S) if sentence]
    count = sum((1 for sentence in sentences if sentence.startswith('I')))
    return count