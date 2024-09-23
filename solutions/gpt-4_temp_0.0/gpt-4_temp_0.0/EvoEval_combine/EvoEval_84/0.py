
from typing import List, Dict

def prefixes_histogram(string: str) -> Dict[str, Dict[str, int]]:
    """ Given a string, return a dictionary where the keys are all the prefixes of the string,
    and the values are dictionaries representing the histograms of the individual letters in each prefix. 
    The histogram dictionaries should contain the letter with the most repetition and the corresponding count.
    If several letters have the same occurrence, include all of them.
    
    Example:
    prefixes_histogram('abc') == {'a': {'a': 1}, 'ab': {'a': 1, 'b': 1}, 'abc': {'a': 1, 'b': 1, 'c': 1}}
    prefixes_histogram('aba') == {'a': {'a': 1}, 'ab': {'a': 1, 'b': 1}, 'aba': {'a': 2}}
    prefixes_histogram('') == {}
    """
    result = {}
    for i in range(1, len(string) + 1):
        prefix = string[:i]
        histogram = Counter(prefix)
        max_count = max(histogram.values(), default=0)
        result[prefix] = {char: count for (char, count) in histogram.items() if count == max_count}
    return result