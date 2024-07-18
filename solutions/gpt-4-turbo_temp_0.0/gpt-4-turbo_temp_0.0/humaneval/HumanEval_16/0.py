

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
    # Convert the string to lowercase (or uppercase) to ensure case-insensitivity
    lower_case_string = string.lower()
    
    # Use a set to keep track of distinct characters
    distinct_characters = set(lower_case_string)
    
    # Return the number of distinct characters
    return len(distinct_characters)
