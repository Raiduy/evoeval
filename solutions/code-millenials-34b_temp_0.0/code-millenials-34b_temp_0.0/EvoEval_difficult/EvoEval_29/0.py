from typing import List, Tuple

def filter_by_prefix_suffix(strings: List[str], prefix_suffix: Tuple[str, str]) -> List[str]:
    (prefix, suffix) = prefix_suffix
    filtered = [string for string in set(strings) if string.startswith(prefix) and string.endswith(suffix)]
    return sorted(filtered)