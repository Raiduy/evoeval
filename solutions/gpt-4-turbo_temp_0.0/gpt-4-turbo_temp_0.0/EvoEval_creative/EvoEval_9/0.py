
def calculate_word_frequency(string: str) -> dict:
    """ Given a string, calculate the frequency of each word present in that string (regardless of case) and return a dictionary with words as keys and their frequencies as values. 
    Words are separated by spaces. Ignore punctuation.
    """
    string = string.lower()
    punctuation = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    string = string.translate(str.maketrans('', '', punctuation))
    words = string.split()
    word_frequency = {}
    for word in words:
        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    return word_frequency