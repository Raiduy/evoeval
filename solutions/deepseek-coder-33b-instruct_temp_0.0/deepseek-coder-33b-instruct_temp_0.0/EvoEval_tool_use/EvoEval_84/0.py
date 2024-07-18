def parse_string(s):
    """This function takes a string as an input and parse it into a list of words.
    A word is defined as a sequence of non-space characters.

    Args:
    s (str): the string to be parsed.

    Returns:
    list: list of words in the string.
    """
    return s.split()

def is_alpha(word):
    """This function takes a word as an input and checks if the word consists of only alphabet letters.

    Args:
    word (str): the word to be checked.

    Returns:
    bool: True if the word contains only letters, False otherwise.
    """
    return word.isalpha()
def count_alpha_words(s):
    """
    Your task is to write a function that counts the number of words in a string that consists of only alphabet letters.
    You need to consider a word as a sequence of non-space characters.

    For example:
    count_alpha_words("Hello world!") => 1
    count_alpha_words("123") => 0
    count_alpha_words("") => 0
    count_alpha_words("Python, Java, C++") => 0
    count_alpha_words("I love Python 3.") => 3

    Args:
    s (str): the string to be analyzed.

    Returns:
    int: the number of words in the string that consists of only letters.
    """
    words = parse_string(s)
    count = 0
    for word in words:
        if is_alpha(word):
            count += 1
    return count