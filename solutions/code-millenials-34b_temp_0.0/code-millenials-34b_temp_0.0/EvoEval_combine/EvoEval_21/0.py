
from typing import List

def base_change_prefixes(x: int, base: int) -> List[str]:

    def int_to_base(n, b):
        if n == 0:
            return '0'
        digits = []
        while n:
            digits.append(str(n % b))
            n //= b
        return ''.join(reversed(digits))
    new_base_num = int_to_base(x, base)
    return [new_base_num[:i] for i in range(1, len(new_base_num) + 1)]