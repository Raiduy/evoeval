
from typing import List, Dict

def prefixes_histogram(string: str) -> Dict[str, Dict[str, int]]:
    result = {}
    for i in range(len(string)):
        prefix = string[:i + 1]
        histogram = {}
        max_count = 0
        for char in prefix:
            histogram[char] = histogram.get(char, 0) + 1
            max_count = max(max_count, histogram[char])
        result[prefix] = {char: count for (char, count) in histogram.items() if count == max_count}
    return result