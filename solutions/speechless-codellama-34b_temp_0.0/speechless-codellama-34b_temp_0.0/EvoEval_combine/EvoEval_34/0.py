from typing import List

def md5_nested_parens(paren_string: str) -> List[str]:
    result = []
    if not paren_string:
        return result
    groups = paren_string.split()
    for group in groups:
        if not is_balanced(group):
            result.append(hashlib.md5(b'None').hexdigest())
            continue
        max_depth = 0
        current_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        result.append(hashlib.md5(str(max_depth).encode()).hexdigest())
    return result