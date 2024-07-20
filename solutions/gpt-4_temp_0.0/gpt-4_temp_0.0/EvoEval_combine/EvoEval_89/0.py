
from typing import List

def md5_substring_filter(strings: List[str], hash_substring: str) -> List[str]:
    """
    Given a list of strings 'strings' and a hash_substring, return a list of strings 
    for which the md5 hash equivalent string contains the hash_substring.
    If 'strings' is an empty list, return None.
    The md5 hash of an empty string should not be considered.

    >>> md5_substring_filter(['Hello world', 'Python', ''], '3e25960a79dbc69b674cd4ec67a72c62')
    ['Hello world']
    >>> md5_substring_filter(['Python', 'Hello', '123', ''], '96')
    ['Hello', '123']
    """
    if not strings:
        return None
    result = []
    for string in strings:
        if string:
            md5_hash = hashlib.md5(string.encode()).hexdigest()
            if hash_substring in md5_hash:
                result.append(string)
    return result