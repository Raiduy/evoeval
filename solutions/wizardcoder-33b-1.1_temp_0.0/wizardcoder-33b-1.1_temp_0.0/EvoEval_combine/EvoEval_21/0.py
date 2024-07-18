
from typing import List

def base_change_prefixes(x: int, base: int) -> List[str]:
    x_in_base = convert_base(x, base)
    prefixes = [x_in_base[:i] for i in range(1, len(x_in_base) + 1)]
    return prefixes