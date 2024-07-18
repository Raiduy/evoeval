def is_valid(word: str) -> bool:
    """ Check if a word is valid. A valid word contains only alphabets and no numbers or special characters.
    >>> is_valid('Hello')
    True
    >>> is_valid('Hello123')
    False
    """
    for character in word:
        if not character.isalpha():
            return False
    return True
def longest_valid_word(sentence: str) -> str:
    """ For a given sentence, return the longest valid word. If there are multiple words of the same maximum length, return the first one.
    A valid word contains only alphabets and no numbers or special characters.
    Return "" if there are no valid words
    
    >>> longest_valid_word("I love programming123 and reading")
    'reading'
    """
    words = sentence.split()
    valid_words = [word for word in words if is_valid(word)]
    if not valid_words:
        return ''
    else:
        return max(valid_words, key=len)