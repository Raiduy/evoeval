from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """ Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    def count_nesting(s: str) -> int:
        max_count = count = 0
        for c in s:
            if c == '(':
                count += 1
                if count > max_count:
                    max_count = count
            elif c == ')':
                count -= 1
        return max_count

    return [count_nesting(group) for group in paren_string.split()]
