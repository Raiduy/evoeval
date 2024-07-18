def is_valid_passport(passport: str) -> bool:
    """ Checks whether a given string is a valid passport number. 
    A valid passport number is defined as having exactly 9 alphanumeric characters.

    >>> is_valid_passport('P12345678')
    True
    >>> is_valid_passport('P123456789')
    False
    >>> is_valid_passport('P12345G78')
    False
    """

    if len(passport) != 9:
        return False
    if not passport.isalnum():
        return False
    return True
from typing import List, Tuple

def process_passport_data(data: str) -> List[Tuple[str, str]]:
    """Parse a string containing passport data and return a list of tuples.
    Each tuple contains the passport number and the name of the passport holder.
    The passport data string is in the format of 'PassportNumber:Name'
    separated by lines.

    Only process valid passport data. A valid passport number is defined as having exactly 9 alphanumeric characters.

    >>> process_passport_data('P12345678:John Doe
X12345678:Jane Doe')
    [('P12345678', 'John Doe')]
    >>> process_passport_data('P12345678:John Doe
A123456789:Jane Doe')
    [('P12345678', 'John Doe')]
    """
    passport_data = []
    for line in data.split('\n'):
        (passport, name) = line.split(':')
        if is_valid_passport(passport):
            passport_data.append((passport, name))
    return passport_data