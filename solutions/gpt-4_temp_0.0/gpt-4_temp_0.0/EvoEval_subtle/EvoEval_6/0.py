
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses. Additionally, return the list in descending order.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [3, 3, 2, 1]
    """
    groups = paren_string.split()
    depths = []
    for group in groups:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif char == ')':
                depth -= 1
        depths.append(max_depth)
    return sorted(depths, reverse=True)