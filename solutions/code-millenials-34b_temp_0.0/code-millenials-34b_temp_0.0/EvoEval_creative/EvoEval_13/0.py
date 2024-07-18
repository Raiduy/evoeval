
from typing import List

def find_rarest_element(elems: List[str]) -> str:
    if not elems:
        return None
    counter = Counter(elems)
    rarest_element = min(counter, key=counter.get)
    return rarest_element