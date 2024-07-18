
def is_bored(S):
    """
    The function takes as input a string S, which contains one or several sentences. 
    A sentence is defined as a string of words that are separated by space characters and terminated by one of the following punctuation marks: '.', '?' or '!'

    The function counts and returns the number of sentences in the string S that start with the word "I", indicating boredom. 
    In other words, a sentence is counted as a boredom if its first word after a sentence termination mark (or at the beginning of the string S) is "I".

    Note: The word "I" might not be the very first character in the sentence, as there might be spaces before it. 

    :param S: A string representing one or several sentences. 
    :return: An integer representing the number of sentences that start with the word "I".

    Examples:
    >>> is_bored("Hello world")
    0
    In the example above, there is only one sentence in the string "Hello world", and it does not start with "I". Therefore, the function returns 0.

    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    In this example, there are three sentences in the string. Only the last one starts with the word "I". Therefore, the function returns 1.
    """
    S += ' '
    count = 0
    sentence_start = 0
    for i in range(len(S)):
        if S[i] in '.?!':
            sentence = S[sentence_start:i].strip()
            if sentence.split()[0] == 'I':
                count += 1
            sentence_start = i + 1
    return count