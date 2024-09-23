
from typing import List

def find_rarest_element(elems: List[str]) -> str:
    """ Find the rarest element in a list of strings. If there are multiple rarest elements, return the one that appears first. 
    If the list is empty, return None.

    >>> find_rarest_element(['apple', 'banana', 'apple', 'orange', 'banana', 'orange', 'apple'])
    'banana'
    >>> find_rarest_element(['cat', 'dog', 'bird', 'cat', 'dog', 'cat'])
    'bird'
    >>> find_rarest_element([])
    None
    """
    if not elems:
        return None
    count = Counter(elems)
    rarest = min(count.items(), key=lambda x: x[1])[0]
    return rarest