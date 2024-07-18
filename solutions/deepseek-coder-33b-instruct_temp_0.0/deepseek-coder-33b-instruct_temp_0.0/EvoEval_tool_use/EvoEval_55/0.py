def helper_is_digit(c: str) -> bool:
    """
    A helper function to check if a character is a digit
    >>> helper_is_digit('3')
    True
    >>> helper_is_digit('a')
    False
    """
    if '0' <= c <= '9':
        return True
    return False


def helper_is_alpha(c: str) -> bool:
    """
    A helper function to check if a character is alphabetic
    >>> helper_is_alpha('b')
    True
    >>> helper_is_alpha('1')
    False
    """
    if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
        return True
    return False
def process_string(s: str) -> str:
    """
    Given a string s, return a new string where each character c is replaced by the next character in the alphabet
    if c is alphabetic, or by the next digit, if c is a digit. 'z' and 'Z' should be replaced by 'a' and 'A' respectively,
    and '9' should be replaced by '0'.
    If c is neither a digit nor an alphabetic character, it should be replaced by a space.
    The function should handle both lower and upper case letters.

    >>> process_string("Hello123")
    'Ifmmp234'
    >>> process_string("Zebra90X")
    'Afcsb01Y'
    >>> process_string("@$%")
    '   '
    """
    result = ''
    for c in s:
        if helper_is_digit(c):
            if c == '9':
                result += '0'
            else:
                result += chr(ord(c) + 1)
        elif helper_is_alpha(c):
            if c == 'z':
                result += 'a'
            elif c == 'Z':
                result += 'A'
            else:
                result += chr(ord(c) + 1)
        else:
            result += ' '
    return result