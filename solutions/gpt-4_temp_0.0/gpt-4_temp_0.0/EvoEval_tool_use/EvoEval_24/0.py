def count_word(word: str) -> bool:
    """
    Helper function to count the number of alphabetical characters in a word (excluding hyphens).
    """
    return len(word.replace("-", ""))
def longest_word(sentence: str) -> str:
    """
    For a given sentence, find the longest valid English word.
    The length is defined as the number of alphabetical characters, excluding hyphens.
    If there are multiple words of the same maximum length, return the first one.
    The sentence may contain punctuation and mixed case letters.
    Note that hyphenated words are considered single words.

    >>> longest_word("I love programming in Python!")
    'programming'
    >>> longest_word("Does it handle non-alphabetical characters appropriately?")
    'non-alphabetical'
    >>> longest_word("Does it handle non alphabetical characters appropriately?")
    'appropriately'
    """
    sentence = re.sub('[' + string.punctuation + ']', ' ', sentence)
    words = sentence.split()
    max_length = 0
    longest_word = ''
    for word in words:
        word_length = count_word(word)
        if word_length > max_length:
            max_length = word_length
            longest_word = word
    return longest_word