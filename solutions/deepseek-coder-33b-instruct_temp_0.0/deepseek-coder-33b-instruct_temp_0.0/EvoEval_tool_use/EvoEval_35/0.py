def is_valid(c: str):
    """ Check if character is valid for parsing.
    Args:
        c (str): The character to check.
    Returns:
        bool: True if valid, False otherwise.
    """
    return c.isalnum() or c.isspace()

def remove_invalid(s: str):
    """ Remove invalid characters from string.
    Args:
        s (str): The string to parse.
    Returns:
        str: The parsed string.
    """
    return "".join(c for c in s if is_valid(c))
def count_unique_words(s: str):
    """
    Return the number of unique words in the string. Words are defined as contiguous sequences 
    of alphanumeric characters, separated by spaces. All words should be transformed to 
    lower case before counting.
    
    Args:
        s (str): The string to parse.
        
    Returns:
        int: The number of unique words.
        
    Example:
    >>> count_unique_words("Hello world, welcome to the universe!")
    6
    >>> count_unique_words("Python is great. Python is fun!")
    4
    """
    s = remove_invalid(s)
    words = s.lower().split()
    return len(set(words))