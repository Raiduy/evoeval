
from typing import List, Optional


def shortest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the shortest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> shortest([])

    >>> shortest(['a', 'b', 'c'])
    'a'
    >>> shortest(['a', 'bb', 'ccc'])
    'a'
    """
    if not strings:
        return None
    shortest_string = strings[0]
    for string in strings:
        if len(string) < len(shortest_string):
            shortest_string = string
    return shortest_string