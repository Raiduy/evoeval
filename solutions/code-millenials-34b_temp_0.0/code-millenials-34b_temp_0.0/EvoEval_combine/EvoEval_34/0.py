from typing import List

def md5_nested_parens(paren_string: str) -> List[str]:
    if not paren_string:
        return []

    def md5(s):
        return hashlib.md5(s.encode()).hexdigest()

    def deepest_level(paren_string):
        count = 0
        max_count = 0
        for c in paren_string:
            if c == '(':
                count += 1
                max_count = max(max_count, count)
            elif c == ')':
                count -= 1
        return str(max_count) if count == 0 else 'None'

    def balanced(paren_string):
        count = 0
        for c in paren_string:
            if c == '(':
                count += 1
            elif c == ')':
                count -= 1
        return count == 0
    groups = re.split('\\s+', paren_string)
    result = []
    for group in groups:
        if balanced(group):
            result.append(md5(deepest_level(group)))
        else:
            result.append(md5('None'))
    return result