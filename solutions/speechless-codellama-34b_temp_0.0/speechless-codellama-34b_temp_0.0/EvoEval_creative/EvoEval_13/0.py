
from typing import List

def find_rarest_element(elems: List[str]) -> str:
    if not elems:
        return None
    counts = {}
    for elem in elems:
        if elem in counts:
            counts[elem] += 1
        else:
            counts[elem] = 1
    rarest_count = min(counts.values())
    for (elem, count) in counts.items():
        if count == rarest_count:
            return elem