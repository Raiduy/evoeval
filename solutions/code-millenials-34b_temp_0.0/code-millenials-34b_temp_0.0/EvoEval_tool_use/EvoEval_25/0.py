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
    """
    if email.count('@') != 1 or email.count('.') != 1 or email.find('@') > email.find('.'):
        return False
    parts = email.split('@')[1].split('.')
    if not parts[0] or not parts[1] or (not parts[2]):
        return False
    return True