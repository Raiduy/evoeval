from typing import List, Tuple

def filter_by_prefix_suffix(strings: List[str], prefix_suffix: Tuple[str, str]) -> List[str]:
    (prefix, suffix) = prefix_suffix
    filtered_strings = [s for s in strings if s.startswith(prefix) and s.endswith(suffix)]
    return sorted(list(set(filtered_strings)))