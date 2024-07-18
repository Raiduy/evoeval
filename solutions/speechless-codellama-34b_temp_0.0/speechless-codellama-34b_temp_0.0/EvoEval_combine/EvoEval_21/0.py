
from typing import List

def base_change_prefixes(x: int, base: int) -> List[str]:
    new_base_x = []
    while x > 0:
        new_base_x.append(str(x % base))
        x //= base
    new_base_x = new_base_x[::-1]
    prefixes = []
    for i in range(len(new_base_x)):
        prefix = ''.join(new_base_x[:i + 1])
        prefixes.append(prefix)
    return prefixes