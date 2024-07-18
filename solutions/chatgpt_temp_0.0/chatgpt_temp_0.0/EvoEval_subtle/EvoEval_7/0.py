
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that do not contain given substring """
    return [s for s in strings if substring not in s]