

def same_chars(s0: str, s1: str) -> bool:
    """
    This function checks if two strings consist of the same set of characters, regardless of their frequency and order in the string. 

    The function takes two arguments, both of which are strings. It will return a boolean value: True if the two strings share the exact same set of characters, and False otherwise. It is important to note that the function does not consider the frequency or order of characters. Therefore, as long as a character exists in both strings, it is counted as a match.
    """
    return set(s0) == set(s1)