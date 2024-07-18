

def is_palindrome(text: str, case_sensitive: bool=True) -> bool:
    if case_sensitive:
        return text == text[::-1]
    else:
        return text.lower() == text.lower()[::-1]