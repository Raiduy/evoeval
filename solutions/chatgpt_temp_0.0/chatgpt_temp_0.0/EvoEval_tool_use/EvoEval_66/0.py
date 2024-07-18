def is_upper(c):
    """Helper Function: Check if the given character is uppercase.
    
    Args:
        c (str): Single character string to be checked.
    
    Returns:
        bool: True if the character is uppercase, False otherwise.
    """
    return c.isupper()

def is_lower(c):
    """Helper Function: Check if the given character is lowercase.
    
    Args:
        c (str): Single character string to be checked.
    
    Returns:
        bool: True if the character is lowercase, False otherwise.
    """
    return c.islower()

def char_to_ascii(c):
    """Helper Function: Convert a character to its ASCII value.
    
    Args:
        c (str): Single character string to be converted.
    
    Returns:
        int: ASCII value of the character.
    """
    return ord(c)
def stringParse(s):
    """Task
    Write a function that takes a string as input, parses the string and returns a tuple.
    The first element of the tuple is the sum of the ASCII codes of the uppercase characters.
    The second element of the tuple is the sum of the ASCII codes of the lowercase characters. 

    Examples: 
        stringParse("") => (0, 0)
        stringParse("abAB") => (131, 195)
        stringParse("abcCd") => (67, 394)
        stringParse("helloE") => (69, 532)
        stringParse("woArBld") => (131, 552)
        stringParse("aAaaaXa") => (153, 485)
    """
    upper_sum = 0
    lower_sum = 0
    for char in s:
        if is_upper(char):
            upper_sum += char_to_ascii(char)
        elif is_lower(char):
            lower_sum += char_to_ascii(char)
    return (upper_sum, lower_sum)