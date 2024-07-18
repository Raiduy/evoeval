
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
    count_dict = {}
    for elem in elems:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    min_count = min(count_dict.values())
    rarest_elems = [k for (k, v) in count_dict.items() if v == min_count]
    for elem in elems:
        if elem in rarest_elems:
            return elem