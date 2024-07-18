
from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses. Additionally, return the list in descending order.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [3, 3, 2, 1]
    """

    def count_nested_parens(s: str) -> int:
        count = max_count = 0
        for c in s:
            if c == '(':
                count += 1
                if count > max_count:
                    max_count = count
            elif c == ')':
                count -= 1
        return max_count
    groups = paren_string.split()
    counts = [count_nested_parens(group) for group in groups]
    counts.sort(reverse=True)
    return counts