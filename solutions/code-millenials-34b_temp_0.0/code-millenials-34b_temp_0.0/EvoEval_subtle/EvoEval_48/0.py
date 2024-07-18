

def is_palindrome(text: str, case_sensitive: bool=True):
    if not case_sensitive:
        text = text.lower()
    return text == text[::-1]