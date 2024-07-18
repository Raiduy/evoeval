

def strlen(string: str) -> int:
    """
    This function returns the length of the given input string. The length of a string is the number of characters 
    that it contains. This includes spaces, digits, alphabets, and special characters. If the input string is empty, 
    the function will return 0, indicating that there are no characters in the string.

    The input to this function should be a string. The function will raise a TypeError if the provided input is not a string.

    The return value of this function is an integer representing the length of the string.

    Here are some examples to demonstrate how this function works:

    >>> strlen('')
    This will return 0 because the input string is empty and therefore contains no characters.

    >>> strlen('abc')
    This will return 3 because the input string 'abc' contains three characters: 'a', 'b', and 'c'.
    """
    if not isinstance(string, str):
        raise TypeError('Input should be a string.')
    return len(string)