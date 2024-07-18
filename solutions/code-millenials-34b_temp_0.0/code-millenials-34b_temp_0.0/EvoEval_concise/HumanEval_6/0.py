from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:

    def max_depth(parens):
        max_count = 0
        count = 0
        for char in parens:
            if char == '(':
                count += 1
                max_count = max(max_count, count)
            elif char == ')':
                count -= 1
        return max_count
    return [max_depth(parens) for parens in paren_string.split()]