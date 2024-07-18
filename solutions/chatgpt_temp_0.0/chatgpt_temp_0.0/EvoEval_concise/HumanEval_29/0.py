from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Return strings from input list that start with specified prefix. """
    return [s for s in strings if s.startswith(prefix)]