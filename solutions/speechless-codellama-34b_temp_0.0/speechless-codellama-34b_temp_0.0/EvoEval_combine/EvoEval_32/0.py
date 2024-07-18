
from typing import List

def circular_shift_nested_parens(input: List[str], shift: int) -> List[int]:
    nesting_depths = [max(0, sum((1 for c in s if c == '('))) for s in input]
    num = int(''.join((str(d) for d in nesting_depths)))
    shifted_num = num * 10 ** shift % 10 ** len(str(num))
    return [int(d) for d in str(shifted_num)]