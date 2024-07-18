
from typing import List

def prime_prefixed_strings(strings: List[str], prefix: str) -> List[str]:
    """
    Return a list of strings from the input list which start with the given prefix and their lengths are prime numbers.
    """
    result = []
    for string in strings:
        if string.startswith(prefix) and is_prime(len(string)):
            result.append(string)
    return result