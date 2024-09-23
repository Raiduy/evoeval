

def is_palindrome(text: str, case_sensitive: bool=True):
    """
    Checks if given string is a palindrome considering case sensitivity according to the provided parameter
    >>> is_palindrome('', True)
    True
    >>> is_palindrome('aba', True)
    True
    >>> is_palindrome('Aba', False)
    True
    >>> is_palindrome('aaaaa', True)
    True
    >>> is_palindrome('zbcd', True)
    False
    """
    if not case_sensitive:
        text = text.lower()
    return text == text[::-1]