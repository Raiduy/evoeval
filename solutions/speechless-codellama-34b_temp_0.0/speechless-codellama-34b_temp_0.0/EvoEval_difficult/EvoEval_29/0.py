from typing import List, Tuple

def filter_by_prefix_suffix(strings: List[str], prefix_suffix: Tuple[str, str]) -> List[str]:
    filtered_strings = []
    for string in strings:
        if string.startswith(prefix_suffix[0]) and string.endswith(prefix_suffix[1]):
            filtered_strings.append(string)
    return sorted(list(set(filtered_strings)))