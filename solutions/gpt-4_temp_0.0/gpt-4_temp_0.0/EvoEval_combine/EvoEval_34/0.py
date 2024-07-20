from typing import List

def md5_nested_parens(paren_string: str) -> List[str]:
    """
    Given a string 'paren_string' that represents multiple groups of nested parentheses separated by spaces,
    compute the md5 hash of the string that represents the deepest level of nesting of parentheses for each group.
    For example '(()())' has deepest level string of '2'.
    Each deepest level is converted to a string before hashing.

    If a group is not balanced (balanced means each open brace is properly closed), return an md5 hash of the string 'None'.
    If 'paren_string' is an empty string, return an empty list.

    An md5 hash is a 32-character hexadecimal number.

    >>> md5_nested_parens('(()()) ((())) () ((())()())')
    ['c81e728d9d4c2f636f067f89cc14862c', 'eccbc87e4b5ce2fe28308fd9f2a7baf3', 'c4ca4238a0b923820dcc509a6f75849b', 'eccbc87e4b5ce2fe28308fd9f2a7baf3']
    """
    if not paren_string:
        return []
    groups = paren_string.split()
    result = []
    for group in groups:
        depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif char == ')':
                if depth == 0:
                    max_depth = 'None'
                    break
                depth -= 1
        if depth != 0:
            max_depth = 'None'
        result.append(hashlib.md5(str(max_depth).encode()).hexdigest())
    return result