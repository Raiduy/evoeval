def parse_string(s):
    '''
    This helper function takes a string and removes all non-alphabet characters.
    
    Args:
    s: A string
    
    Returns:
    A string having only alphabet characters.
    
    Example:
    
    parse_string("Hello, World!") ➞ "HelloWorld"
    parse_string("Pyth0n Pr0gramm!ng") ➞ "PythonProgramming"
    '''
    return ''.join(c for c in s if c.isalpha())
def rearrange_string(s1, s2):
    """
    Create a function that takes 2 strings.
    The function should return a new string such that the characters from the first string should appear before the characters from the second string in the new string.
    Ignore all non-alphabet characters in the input strings.

    If the sum of ASCII values of the characters in the first string is less than or equal to the sum of ASCII values of the characters in the second string,
    then in the new string, the order of characters should be in ascending order.

    If the sum of ASCII values of the characters in the first string is greater than the sum of ASCII values of the characters in the second string,
    then in the new string, the order of characters should be in descending order.


    Examples
    rearrange_string("Hello, World!", "Python Programming") ➞ "HWdellloorPPagghimmnnoorrty"

    rearrange_string("Good Morning", "Hello") ➞ "rooonnigdMGolleH"

    rearrange_string("Data Science", "Artificial Intelligence") ➞ "DSaacceeintAIacceeefgiiiillnrtt"

    rearrange_string("Python 3.9", "Python 2.7") ➞ "PhnotyPhnoty"
    """
    s1 = parse_string(s1)
    s2 = parse_string(s2)
    ascii_sum_s1 = sum((ord(c) for c in s1))
    ascii_sum_s2 = sum((ord(c) for c in s2))
    if ascii_sum_s1 <= ascii_sum_s2:
        return ''.join(sorted(s1 + s2))
    else:
        return ''.join(sorted(s1 + s2, reverse=True))