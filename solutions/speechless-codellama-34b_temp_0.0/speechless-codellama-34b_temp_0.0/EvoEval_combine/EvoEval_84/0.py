
from typing import List, Dict

def prefixes_histogram(string: str) -> Dict[str, Dict[str, int]]:
    result = {}
    for i in range(len(string)):
        prefix = string[:i + 1]
        histogram = {}
        for j in range(len(prefix)):
            letter = prefix[j]
            if letter in histogram:
                histogram[letter] += 1
            else:
                histogram[letter] = 1
        max_count = max(histogram.values())
        max_letters = [k for (k, v) in histogram.items() if v == max_count]
        result[prefix] = {k: v for (k, v) in histogram.items() if k in max_letters}
    return result