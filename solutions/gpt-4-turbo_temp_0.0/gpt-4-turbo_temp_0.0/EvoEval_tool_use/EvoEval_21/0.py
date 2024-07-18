def strip_spaces(string: str) -> str:
    """Remove leading and trailing spaces from the string."""
    return string.strip()

def to_lowercase(string: str) -> str:
    """Convert all characters in the string to lowercase."""
    return string.lower()

def remove_non_alphanumeric(string: str) -> str:
    """Remove all non-alphanumeric characters from the string."""
    return ''.join(ch for ch in string if ch.isalnum())
from typing import List

def get_cleaned_strings(strings: List[str]) -> List[str]:
    """ Given a list of strings, return a new list where each string is
    converted into lowercase, stripped of both leading and trailing spaces and 
    all non-alphanumeric characters are removed.

    >>> get_cleaned_strings([" Hello World! ", "Pyth0n Pr0gr4mm!ng ", "   PYTHON   "])
    ['helloworld', 'pyth0npr0gr4mmng', 'python']
    """
    cleaned_strings = []
    for string in strings:
        cleaned_string = strip_spaces(string)
        cleaned_string = to_lowercase(cleaned_string)
        cleaned_string = remove_non_alphanumeric(cleaned_string)
        cleaned_strings.append(cleaned_string)
    return cleaned_strings