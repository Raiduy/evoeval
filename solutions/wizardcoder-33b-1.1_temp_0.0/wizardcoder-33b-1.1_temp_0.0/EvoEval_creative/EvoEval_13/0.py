
from typing import List

def find_rarest_element(elems: List[str]) -> str:
    if not elems:
        return None
    count_dict = {}
    for elem in elems:
        if elem in count_dict:
            count_dict[elem] += 1
        else:
            count_dict[elem] = 1
    min_count = min(count_dict.values())
    for elem in elems:
        if count_dict[elem] == min_count:
            return elem