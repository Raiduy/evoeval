
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I" and ends with the word "boredom".
    Sentences are delimited by '.', '?' or '!'.
    
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I am experiencing boredom")
    1
    """
    sentences = S.split('. ') + S.split('? ') + S.split('! ')
    count = 0
    for sentence in sentences:
        words = sentence.split()
        if words[0] == 'I' and words[-1] == 'boredom':
            count += 1
    return count