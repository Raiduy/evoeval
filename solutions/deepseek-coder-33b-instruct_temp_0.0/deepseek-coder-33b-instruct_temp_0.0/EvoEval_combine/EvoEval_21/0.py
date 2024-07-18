
from typing import List

def base_change_prefixes(x: int, base: int) -> List[str]:
    base_x = ''
    while x > 0:
        base_x = str(x % base) + base_x
        x //= base
    prefixes = [base_x[0:i] for i in range(1, len(base_x) + 1)]
    return prefixes