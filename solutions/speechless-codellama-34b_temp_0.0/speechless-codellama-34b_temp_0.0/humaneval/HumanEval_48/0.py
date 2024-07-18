

def is_palindrome(text: str) -> bool:
    """
    Checks if given string is a palindrome
    """
    return text == text[::-1]
