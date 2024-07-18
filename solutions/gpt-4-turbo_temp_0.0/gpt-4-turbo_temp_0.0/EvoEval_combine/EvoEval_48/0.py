
from typing import List

def prime_prefixed_strings(strings: List[str], prefix: str) -> List[str]:
    """
    Write a function that takes a list of strings and a prefix, it should return a list of 
    strings from the input list which start with the given prefix and their lengths are prime numbers.
    
    Examples
    prime_prefixed_strings([], 'a') == []
    prime_prefixed_strings(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']
    prime_prefixed_strings(['abcd', 'bcd', 'cde', 'array'], 'a') == ['array']
    prime_prefixed_strings(['apple', 'avocado', 'banana', 'apricot'], 'a') == ['apple', 'avocado', 'apricot']
    """
    return [s for s in strings if s.startswith(prefix) and is_prime(len(s))]