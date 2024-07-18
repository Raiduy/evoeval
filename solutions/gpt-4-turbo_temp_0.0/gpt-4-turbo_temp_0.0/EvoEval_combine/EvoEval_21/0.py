
from typing import List

def base_change_prefixes(x: int, base: int) -> List[str]:
    if x == 0:
        return ['0']
    digits = []
    while x:
        digits.append(str(x % base))
        x //= base
    base_repr = ''.join(reversed(digits))
    prefixes = [base_repr[:i] for i in range(1, len(base_repr) + 1)]
    return prefixes