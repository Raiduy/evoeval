
from typing import List


def filter_by_suffix(strings: List[str], suffix: str) -> List[str]:
    """ Filter an input list of strings only for ones that end with a given suffix. """
    return [s for s in strings if s.endswith(suffix)]