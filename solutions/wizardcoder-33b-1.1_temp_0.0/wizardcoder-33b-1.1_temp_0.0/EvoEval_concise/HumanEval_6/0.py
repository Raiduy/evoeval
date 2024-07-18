from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Takes a string representing groups of nested parentheses separated by spaces.
    Returns a list representing the deepest level of nesting in each group.
    
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    results = []
    for group in groups:
        current_level = 0
        max_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                if current_level > max_level:
                    max_level = current_level
            elif char == ')':
                current_level -= 1
        results.append(max_level)
    return results