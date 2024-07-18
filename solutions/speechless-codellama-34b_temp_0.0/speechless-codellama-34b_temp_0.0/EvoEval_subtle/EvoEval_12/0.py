
from typing import List, Optional


def shortest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    shortest_string = strings[0]
    for string in strings:
        if len(string) < len(shortest_string):
            shortest_string = string
    return shortest_string