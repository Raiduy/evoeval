from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Returns the longest string from a list, or the first one in case of a tie. If list is empty, returns None.
    >>> longest([])
    
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:
        return None
    max_length = len(strings[0])
    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string