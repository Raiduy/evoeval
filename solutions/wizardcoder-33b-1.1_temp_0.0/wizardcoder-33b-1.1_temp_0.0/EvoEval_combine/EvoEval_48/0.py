
from typing import List

def prime_prefixed_strings(strings: List[str], prefix: str) -> List[str]:
    """
    Function that takes a list of strings and a prefix, it should return a list of 
    strings from the input list which start with the given prefix and their lengths are prime numbers.
    """
    return [s for s in strings if s.startswith(prefix) and is_prime(len(s))]