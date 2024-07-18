def correct_bracketing_advanced(brackets: str, scope: tuple):
    stack = []
    (scope_open, scope_close) = scope
    for bracket in brackets:
        if bracket == scope_open:
            stack.append(bracket)
        elif bracket == scope_close:
            if not stack or stack[-1] != scope_open:
                return False
            stack.pop()
    return not stack