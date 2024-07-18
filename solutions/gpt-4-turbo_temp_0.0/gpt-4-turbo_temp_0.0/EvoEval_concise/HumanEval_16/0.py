

def count_distinct_characters(string: str) -> int:
    """ Returns the count of unique case-insensitive characters in a given string.
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    lower_case_string = string.lower()
    unique_characters = set(lower_case_string)
    return len(unique_characters)