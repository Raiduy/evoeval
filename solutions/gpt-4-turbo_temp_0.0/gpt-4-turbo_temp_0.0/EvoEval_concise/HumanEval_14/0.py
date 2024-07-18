from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Generates a list of prefixes for the input string in ascending length order.
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    return [string[:i + 1] for i in range(len(string))]