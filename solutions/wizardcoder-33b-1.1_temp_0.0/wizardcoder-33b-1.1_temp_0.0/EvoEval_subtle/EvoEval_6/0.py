
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:

    def count_depth(s: str) -> int:
        max_depth = current_depth = 0
        for c in s:
            if c == '(':
                current_depth += 1
                max_depth = max(max_depth, current_depth)
            elif c == ')':
                current_depth -= 1
        return max_depth
    return sorted([count_depth(group) for group in paren_string.split()], reverse=True)