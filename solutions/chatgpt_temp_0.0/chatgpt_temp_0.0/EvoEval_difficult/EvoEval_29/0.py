from typing import List, Tuple

def filter_by_prefix_suffix(strings: List[str], prefix_suffix: Tuple[str, str]) -> List[str]:
    (prefix, suffix) = prefix_suffix
    filtered_strings = []
    for string in strings:
        if string.lower().startswith(prefix.lower()) and string.lower().endswith(suffix.lower()):
            filtered_strings.append(string)
    filtered_strings = list(set(filtered_strings))
    filtered_strings.sort()
    return filtered_strings