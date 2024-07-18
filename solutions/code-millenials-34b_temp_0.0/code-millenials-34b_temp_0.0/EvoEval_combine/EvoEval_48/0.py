
from typing import List

def prime_prefixed_strings(strings: List[str], prefix: str) -> List[str]:
    """Return a list of strings that start with the given prefix and have prime lengths."""
    return [s for s in strings if s.startswith(prefix) and is_prime(len(s))]