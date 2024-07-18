from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Takes a string representing groups of nested parentheses separated by spaces.
    Returns a list representing the deepest level of nesting in each group.
    
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
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
    return depths