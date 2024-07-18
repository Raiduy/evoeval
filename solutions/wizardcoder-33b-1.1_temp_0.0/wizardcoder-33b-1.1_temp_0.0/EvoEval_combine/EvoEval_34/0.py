from typing import List

def md5_nested_parens(paren_string: str) -> List[str]:
    if not paren_string:
        return []
    groups = paren_string.split()
    result = []
    for group in groups:
        if not is_balanced(group):
            result.append(hashlib.md5('None'.encode()).hexdigest())
        else:
            result.append(hashlib.md5(str(max_depth(group)).encode()).hexdigest())
    return result