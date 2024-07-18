from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of a list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:  # Check if the list is empty
        return None
    # Use the max function with key=len to find the longest string
    return max(strings, key=len)
