
from typing import List, Dict

def prefixes_histogram(string: str) -> Dict[str, Dict[str, int]]:
    result = {}
    for i in range(len(string)):
        prefix = string[:i + 1]
        histogram = {}
        for letter in prefix:
            histogram[letter] = histogram.get(letter, 0) + 1
        result[prefix] = histogram
    return result