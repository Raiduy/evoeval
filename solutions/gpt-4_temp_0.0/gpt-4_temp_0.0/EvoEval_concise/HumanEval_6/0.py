from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Takes a string representing groups of nested parentheses separated by spaces.
    Returns a list representing the deepest level of nesting in each group.
    
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    depths = []
    depth = 0
    max_depth = 0
    for char in paren_string:
        if char == '(':
            depth += 1
            max_depth = max(max_depth, depth)
        elif char == ')':
            depth -= 1
        elif char == ' ' and max_depth > 0:
            depths.append(max_depth)
            max_depth = 0
    if max_depth > 0:
        depths.append(max_depth)
    return depths