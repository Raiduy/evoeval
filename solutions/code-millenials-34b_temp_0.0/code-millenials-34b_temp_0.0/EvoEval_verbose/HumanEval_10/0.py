
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that can be formed beginning with a supplied string.

    This function uses a simple algorithm to determine how to make the given string into a palindrome, which
    is a string that reads the same forward and backward. The algorithm proceeds through the following steps:
    1. It first finds the longest suffix (ending segment) of the supplied string that itself is a palindrome.
    2. It then appends to the end of the original string the reversed string of the prefix 
       (beginning segment) that comes before this palindromic suffix. 

    As a result, the returning string is the shortest possible palindrome that starts with the given string.
    Should the input string already be a palindrome, the function will simply return the original string.

    This function is case-sensitive and does not alter the case of the lettering in the original string.

    Parameters:
    string (str): The string to be made into a palindrome.

    Returns:
    str: The shortest possible palindrome that starts with the input string.

    Doctest:
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """
    if is_palindrome(string):
        return string
    for i in range(len(string)):
        if is_palindrome(string[i:]):
            return string + string[:i][::-1]
    return string + string[::-1]