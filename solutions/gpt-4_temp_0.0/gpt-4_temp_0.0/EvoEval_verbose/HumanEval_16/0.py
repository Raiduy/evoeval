

def count_distinct_characters(string: str) -> int:
    """
    This function takes a string as its input and returns the total number of distinct characters it contains, 
    without considering the case of the characters. That means, 'a' and 'A' will be considered as the same character.

    It uses the built-in Python data structure set to accomplish this task. 
    The set data structure in Python, by definition, contains unique elements, 
    which makes it perfect for this sort of problem where we need to count the number of unique items.
    
    Parameters:
    string (str): The input string whose distinct characters need to be counted. 

    Returns:
    int: The number of distinct characters in the input string irrespective of their case.

    Examples:
    >>> count_distinct_characters('xyzXYZ')
    3

    Explanation: Although visually the string appears to have 6 characters, 
    but since we are not considering case, 'x' and 'X' are considered as the same character. 
    Similarly 'y' and 'Y', 'z' and 'Z' are considered as same characters. Hence, the total number of distinct characters is 3.

    >>> count_distinct_characters('Jerry')
    4

    Explanation: In this case, the distinct characters are 'J', 'e', 'r', 'y'. 
    Although 'r' appears twice, it is considered as one unique character. Hence, the total number of distinct characters is 4.
    """
    return len(set(string.lower()))