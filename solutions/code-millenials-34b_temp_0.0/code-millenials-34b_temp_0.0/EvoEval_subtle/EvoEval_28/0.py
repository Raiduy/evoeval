
from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string, separated by a comma.
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'a,b,c'
    """
    return ','.join(strings)