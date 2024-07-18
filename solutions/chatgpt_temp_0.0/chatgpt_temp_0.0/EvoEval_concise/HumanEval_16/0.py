

def count_distinct_characters(string: str) -> int:
    """ Returns the count of unique case-insensitive characters in a given string.
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string = string.lower()
    unique_chars = set()
    for char in string:
        unique_chars.add(char)
    return len(unique_chars)