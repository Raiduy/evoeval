from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Return strings from input list that start with specified prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]