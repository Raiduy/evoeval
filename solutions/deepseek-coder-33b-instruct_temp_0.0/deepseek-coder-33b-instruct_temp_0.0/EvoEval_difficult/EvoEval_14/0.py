from typing import List, Tuple

def all_prefix_suffix_pairs(string: str, min_length: int) -> List[Tuple[str, str]]:
    pairs = []
    for i in range(min_length, len(string)):
        for j in range(i + min_length, len(string) + 1):
            pairs.append((string[:i], string[i:j]))
    pairs.sort(key=lambda x: (len(x[0]), x[0], len(x[1]), x[1]))
    return pairs