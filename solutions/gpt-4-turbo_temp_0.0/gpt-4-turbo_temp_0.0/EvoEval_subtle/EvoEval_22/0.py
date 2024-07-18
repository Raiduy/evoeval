
from typing import List, Any


def filter_even_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for even integers
    >>> filter_even_integers(['a', 3.14, 5, 6])
    [6]
    >>> filter_even_integers([1, 2, 3, 'abc', {}, []])
    [2]
    """
    even_integers = []
    for value in values:
        if isinstance(value, int) and value % 2 == 0:
            even_integers.append(value)
    return even_integers