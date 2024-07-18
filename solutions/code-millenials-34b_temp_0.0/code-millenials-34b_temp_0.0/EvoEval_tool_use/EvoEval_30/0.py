def parse_input(input_str: str) -> list:
    """
    This function receives a string and returns a list of strings. The input string should contain words separated by 
    space(s). The function will split the input string by space(s) and return the list of words.
    >>> parse_input('Hello world from python')
    ['Hello', 'world', 'from', 'python']
    >>> parse_input('  This is a    test   ')
    ['This', 'is', 'a', 'test']
    """
    return [word for word in input_str.split() if word]
def get_long_words(input_str: str, min_length: int) -> list:
    """
    This function receives a string and a minimum word length and returns a list of words that have lengths greater 
    than or equal to the minimum length. The input string contains words separated by space(s).
    If there are no words of length greater than or equal to the minimum length, the function should return an empty list.
    >>> get_long_words('Hello world from python', 5)
    ['Hello', 'world', 'python']
    >>> get_long_words('This is a test', 5)
    ['']
    """
    return [word for word in parse_input(input_str) if len(word) >= min_length]