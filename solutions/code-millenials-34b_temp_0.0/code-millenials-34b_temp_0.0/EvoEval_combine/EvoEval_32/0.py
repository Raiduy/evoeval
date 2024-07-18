
from typing import List

def circular_shift_nested_parens(input: List[str], shift: int) -> List[int]:

    def max_depth(s: str) -> int:
        max_d = d = 0
        for c in s:
            if c == '(':
                d += 1
                max_d = max(max_d, d)
            elif c == ')':
                d -= 1
        return max_d
    depths = [max_depth(s) for s in input]
    depths_str = ''.join(map(str, depths))
    if shift >= len(depths_str):
        depths_str = depths_str[::-1]
    else:
        depths_str = depths_str[-shift:] + depths_str[:-shift]
    return list(map(int, depths_str))