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
    else:
        return max(strings, key=len)