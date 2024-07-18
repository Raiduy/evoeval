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
    words = re.findall("\\b\\w[\\w-]*\\'*\\w*\\b", sentence)
    longest_word = ''
    longest_length = 0
    for word in words:
        length = count_word(word)
        if length > longest_length:
            longest_word = word
            longest_length = length
    return longest_word