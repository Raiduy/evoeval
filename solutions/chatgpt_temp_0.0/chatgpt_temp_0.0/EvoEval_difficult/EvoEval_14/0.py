from typing import List, Tuple

def all_prefix_suffix_pairs(string: str, min_length: int) -> List[Tuple[str, str]]:
    pairs = []
    for i in range(min_length, len(string) - min_length + 1):
        prefix = string[:i]
        suffix = string[-i:]
        if prefix != suffix:
            pairs.append((prefix, suffix))
    pairs.sort(key=lambda x: (len(x[0]), x[0]))
    return pairs