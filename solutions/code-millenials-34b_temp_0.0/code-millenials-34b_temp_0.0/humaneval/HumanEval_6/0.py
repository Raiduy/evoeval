from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    def max_depth(s: str) -> int:
        max_count = count = 0
        for c in s:
            if c == '(':
                count += 1
                max_count = max(max_count, count)
            elif c == ')':
                count -= 1
        return max_count
    
    return [max_depth(s) for s in paren_string.split()]

