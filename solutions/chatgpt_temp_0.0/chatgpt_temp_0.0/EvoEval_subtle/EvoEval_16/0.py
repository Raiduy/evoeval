
def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (case-sensitive) does it consist of.
    >>> count_distinct_characters('xyzXYZ')
    6
    >>> count_distinct_characters('Jerry')
    4
    """
    distinct_characters = set(string)
    return len(distinct_characters)