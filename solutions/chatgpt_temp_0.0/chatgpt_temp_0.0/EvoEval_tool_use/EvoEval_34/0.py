def parse_string(s: str):
    """Split a string into words
    Args:
        s (str): Input string
    Returns:
        list: List of words in the string
    """
    return s.split()


def is_digit(s: str):
    """Check if a string is a number or not 
    Args:
        s (str): Input string
    Returns:
        bool: True if the string is a number, False otherwise
    """
    return s.isdigit()
def sorted_values(s: str):
    """Return sorted list of unique integers found in the input string. The string can contain words and numbers
    >>> sorted_values("123 apple 456 apple 123 456 banana 789")
    [123, 456, 789]
    Args:
        s (str): Input string
    Returns:
        list: Sorted list of unique numbers found in the string
    """
    numbers = []
    for word in s.split():
        if is_digit(word):
            numbers.append(int(word))
    return sorted(set(numbers))