from typing import List, Tuple

def all_prefix_suffix_pairs(string: str, min_length: int) -> List[Tuple[str, str]]:
    result = []
    for i in range(min_length, len(string)):
        for j in range(min_length, len(string) - i + 1):
            result.append((string[:i], string[-j:]))
    result.sort(key=lambda x: (len(x[0]), x[0], len(x[1]), x[1]))
    return result