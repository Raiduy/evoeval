
from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from longest to shortest of the input string
    >>> all_prefixes('abc')
    ['abc', 'ab', 'a']
    """
    return [string[:i] for i in range(len(string), 0, -1)]