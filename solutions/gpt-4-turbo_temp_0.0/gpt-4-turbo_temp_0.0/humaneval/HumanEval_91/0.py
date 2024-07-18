
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
    
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Split the string into sentences using the specified delimiters
    sentences = []
    temp_sentence = ''
    for char in S:
        if char in '.?!':
            sentences.append(temp_sentence.strip())
            temp_sentence = ''
        else:
            temp_sentence += char
    if temp_sentence:  # Add the last sentence if there's any
        sentences.append(temp_sentence.strip())

    # Count the sentences that start with "I "
    boredom_count = 0
    for sentence in sentences:
        if sentence.startswith("I "):
            boredom_count += 1

    return boredom_count