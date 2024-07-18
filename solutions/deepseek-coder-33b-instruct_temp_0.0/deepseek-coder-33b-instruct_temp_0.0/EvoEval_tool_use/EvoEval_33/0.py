def helper_is_valid(string):
    """
    This function checks whether the provided string is valid
    according to the following rules:
    - The string only contains alphabetical characters
    - The string length is at least 2 
    - The string first and last character are the same
    It returns True if the string is valid and False otherwise.

    >>> helper_is_valid("racecar")
    True
    >>> helper_is_valid("apple")
    False
    """
    if not string.isalpha():
        return False
    if len(string) < 2:
        return False
    if string[0] != string[-1]:
        return False
    return True

def helper_reverse_string(string):
    """
    This function reverses the provided string and returns the result.

    >>> helper_reverse_string("racecar")
    'racecar'
    >>> helper_reverse_string("apple")
    'elppa'
    """
    return string[::-1]
def modify_strings(strings: list):
    """
    This function takes a list of strings and modifies each string according to
    the following rules:
    - If the string is valid:
        - The string only contains alphabetical characters
        - The string length is at least 2
        - The string first and last character are the same
      then it is reversed
    - If the string is not valid, it is left unchanged
    The function returns a new list where each string has been modified
    according to these rules.

    >>> modify_strings(["hello", "apple", "racecar"])
    ['hello', 'apple', 'racecar']
    >>> modify_strings(["aha", "banana", "mom"])
    ['aha', 'banana', 'mom']
    """

    def helper_is_valid(string):
        """
        This function checks whether the provided string is valid
        according to the following rules:
        - The string only contains alphabetical characters
        - The string length is at least 2 
        - The string first and last character are the same
        It returns True if the string is valid and False otherwise.

        >>> helper_is_valid("racecar")
        True
        >>> helper_is_valid("apple")
        False
        """
        if not string.isalpha():
            return False
        if len(string) < 2:
            return False
        if string[0] != string[-1]:
            return False
        return True

    def helper_reverse_string(string):
        """
        This function reverses the provided string and returns the result.

        >>> helper_reverse_string("racecar")
        'racecar'
        >>> helper_reverse_string("apple")
        'elppa'
        """
        return string[::-1]
    result = []
    for string in strings:
        if helper_is_valid(string):
            result.append(helper_reverse_string(string))
        else:
            result.append(string)
    return result