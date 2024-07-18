
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:

    def max_depth(s: str) -> int:
        max_d = d = 0
        for c in s:
            if c == '(':
                d += 1
                max_d = max(max_d, d)
            elif c == ')':
                d -= 1
        return max_d
    return sorted([max_depth(s) for s in paren_string.split()], reverse=True)