
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
    import re
    sentences = re.split('[.?!]', S)
    boredoms = [sentence for sentence in sentences if sentence.strip().startswith('I') and sentence.strip().endswith('boredom')]
    return len(boredoms)