def correct_bracketing_advanced(brackets: str, scope: tuple):
    stack = []
    for bracket in brackets:
        if bracket == scope[0]:
            stack.append(bracket)
        elif bracket == scope[1]:
            if not stack or stack.pop() != scope[0]:
                return False
    return not stack