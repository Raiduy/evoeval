

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that ends with a supplied string.
    Algorithm idea is simple:
    - Find the longest prefix of supplied string that is a palindrome.
    - Append to the start of the string reverse of a string suffix that comes after the palindromic prefix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'tacat'
    >>> make_palindrome('cata')
    'atacata'
    """
    if is_palindrome(string):
        return string
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            return string[i - 1::-1] + string
    return string