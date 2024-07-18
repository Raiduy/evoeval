

def count_distinct_characters(string: str) -> int:
    """ Returns the count of unique case-insensitive characters in a given string.
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    string_lower = string.lower()
    return len(set(string_lower))