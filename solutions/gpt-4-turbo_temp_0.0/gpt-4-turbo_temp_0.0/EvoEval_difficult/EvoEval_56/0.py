def correct_bracketing_advanced(brackets: str, scope: tuple) -> bool:
    stack = []
    bracket_pairs = {'<': '>', '[': ']', '{': '}', '(': ')'}
    opening_brackets = set(bracket_pairs.keys())
    closing_brackets = set(bracket_pairs.values())
    for char in brackets:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if not stack or bracket_pairs[stack[-1]] != char:
                return False
            else:
                stack.pop()
    if stack:
        return False
    stack = []
    (opening_scope, closing_scope) = scope
    for char in brackets:
        if char == opening_scope:
            stack.append(char)
        elif char == closing_scope:
            if not stack:
                return False
            stack.pop()
    if stack:
        return False
    return True