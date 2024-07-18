def count_capital_letters(s: str) -> int:
    """Helper function to count the number of capital letters in a string.
    """
    return sum(1 for c in s if c.isupper())


def check_alphanumeric(s: str) -> bool:
    """Helper function to check if a string is alphanumeric.
    """
    return s.isalnum()
def evaluate_string(s: str) -> int:
    """Determine the number of words in a string that are purely alphanumeric and have at least one capital letter.
    
    A word is defined as a series of alphanumeric characters surrounded by spaces or at the start/end of the string.

    >>> evaluate_string("Hello World!")
    1
    >>> evaluate_string("This Is A test String 123.")
    3
    >>> evaluate_string("no Capital letter here")
    0
    """
    words = s.split()
    valid_words_count = 0
    for word in words:
        word_alnum = ''.join((char for char in word if char.isalnum()))
        if check_alphanumeric(word_alnum) and count_capital_letters(word_alnum) > 0:
            valid_words_count += 1
    return valid_words_count