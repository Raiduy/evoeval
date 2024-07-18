def convert_to_lower(word: str):
    """
    A helper function that converts a given word into lowercase.
    """
    return word.lower()

def remove_punctuation(word: str):
    """
    A helper function that removes punctuations from a given word.
    """
    import string
    return word.translate(str.maketrans('', '', string.punctuation))

def sort_word(word: str):
    """
    A helper function that sorts the characters in a word alphabetically.
    """
    return ''.join(sorted(word))

def clean_word(word: str):
    """
    A helper function that cleans a word by converting it to lowercase, removing punctuations, and sorting its characters.
    """
    lower_word = convert_to_lower(word)
    no_punct_word = remove_punctuation(lower_word)
    sorted_word = sort_word(no_punct_word)
    sorted_word = "".join(sorted_word.split())
    return sorted_word
def is_homophone(s0: str, s1: str):
    """
    Check if two words are homophones (words that are pronounced the same way but may have different meanings or spellings). 
    Note: This function only considers words as homophones if they contain the same letters in the same proportions, 
    irrespective of their order, case, or any punctuation marks they may include. 
    
    >>> is_homophone('Listen', 'Silent')
    True
    >>> is_homophone('Dormitory', 'Dirty Room')
    True
    >>> is_homophone('Astronomer', 'Moon starer')
    True
    >>> is_homophone('Conversation', 'Voices rant on')
    True
    >>> is_homophone('School master', 'The classroom')
    True
    >>> is_homophone('Election results', 'Lies – let’s recount')
    False
    >>> is_homophone('The eyes', 'They see')
    True
    >>> is_homophone('A gentleman', 'Elegant man')
    True
    """
    clean_s0 = clean_word(s0)
    clean_s1 = clean_word(s1)
    return clean_s0 == clean_s1