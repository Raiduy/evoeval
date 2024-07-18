from typing import List, Tuple

def all_prefix_suffix_pairs(string: str, min_length: int) -> List[Tuple[str, str]]:
    prefix_suffix_pairs = []
    for i in range(len(string)):
        for j in range(i + min_length, len(string) + 1):
            prefix = string[:j]
            suffix = string[i:]
            if len(prefix) >= min_length and len(suffix) >= min_length:
                prefix_suffix_pairs.append((prefix, suffix))
    prefix_suffix_pairs.sort(key=lambda x: (len(x[0]), x[0]))
    return prefix_suffix_pairs