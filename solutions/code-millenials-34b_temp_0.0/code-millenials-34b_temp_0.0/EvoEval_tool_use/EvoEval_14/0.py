from typing import List

def validate_isbn(isbn: str) -> bool:
    """
    Helper function that checks if a string is a valid ISBN-10 or ISBN-13
    It assumes that the ISBN string is either 10 or 13 characters long with no hyphens.
    This function does not perform a thorough validation of the ISBN format,
    but merely checks the length and checks that all characters are digits
    (the last character in an ISBN-10 may be an 'X').

    >>> validate_isbn('0123456789')
    True
    >>> validate_isbn('01234567890AB')
    False
    >>> validate_isbn('0123456789X')
    True
    """
    if len(isbn) not in [10, 13]:
        return False
    if len(isbn) == 13:
        return isbn.isdigit()
    if not isbn[:-1].isdigit():
        return False
    if len(isbn) == 10 and isbn[-1] not in "0123456789X":
        return False
    return True

from typing import List

def find_valid_isbns(isbn_list: List[str]) -> List[str]:
    """
    Given a list of strings, return a list of all valid ISBNs.
    An ISBN is a 10 or 13 character string. The first 9 characters are all digits. 
    The last character can be 0-9 or 'X'. For a 13 character ISBN, all characters are digits.
    
    >>> find_valid_isbns(['0123456789', '01234567890AB', '012345678X'])
    ['0123456789', '012345678X']
    """
    return [isbn for isbn in isbn_list if validate_isbn(isbn)]