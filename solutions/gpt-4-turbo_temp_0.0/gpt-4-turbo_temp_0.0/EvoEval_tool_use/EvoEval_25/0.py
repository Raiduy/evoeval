from typing import List

def count_char(email: str, char: str) -> int:
    """ Count the occurrence of a specific character in a string """
    return email.count(char)

def split_email(email: str) -> List[str]:
    """ Split an email into parts by '@' and '.' """
    return email.split('@')[1].split('.')
def valid_email(email: str) -> bool:
    """ Check if an email is valid.
    An email is valid if it contains only one '@' and one '.' after '@', and there are at least one character before '@', between '@' and '.', and after '.'
    >>> valid_email("test@email.com")
    True
    >>> valid_email("invalid_email.com")
    False
    """
    if email.count('@') != 1:
        return False
    (local, domain) = email.split('@')
    if not local or '.' not in domain:
        return False
    domain_parts = domain.split('.')
    if len(domain_parts) < 2:
        return False
    if not all(domain_parts):
        return False
    return True