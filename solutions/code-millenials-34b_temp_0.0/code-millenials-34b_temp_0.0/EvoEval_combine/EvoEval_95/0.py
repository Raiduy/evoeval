
from typing import List

def filter_sort_strings(strings: List[str], substring: str) -> List[str]:
    filtered_strings = [s for s in strings if substring in s and len(s) % 2 == 0]
    sorted_strings = sorted(filtered_strings, key=lambda x: (len(x), x))
    return sorted_strings