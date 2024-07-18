from typing import List

def md5_nested_parens(paren_string: str) -> List[str]:

    def is_balanced(s: str) -> bool:
        count = 0
        for char in s:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
                if count < 0:
                    return False
        return count == 0

    def deepest_level(s: str) -> int:
        max_depth = 0
        current_depth = 0
        for char in s:
            if char == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif char == ')':
                current_depth -= 1
        return max_depth
    if not paren_string:
        return []
    result = []
    groups = paren_string.split()
    for group in groups:
        if is_balanced(group):
            depth = str(deepest_level(group))
            result.append(hashlib.md5(depth.encode()).hexdigest())
        else:
            result.append(hashlib.md5('None'.encode()).hexdigest())
    return result