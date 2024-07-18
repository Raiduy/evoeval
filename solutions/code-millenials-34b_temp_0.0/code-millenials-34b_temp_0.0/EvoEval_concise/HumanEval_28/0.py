from typing import List


def concatenate(strings: List[str]) -> str:
    """
    Join list of strings into one string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    return ''.join(strings)