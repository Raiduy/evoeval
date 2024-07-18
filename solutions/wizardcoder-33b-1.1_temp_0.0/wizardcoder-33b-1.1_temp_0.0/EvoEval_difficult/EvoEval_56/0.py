def correct_bracketing_advanced(brackets: str, scope: tuple):
    stack = []
    open_brackets = {scope[0]: scope[1]}
    close_brackets = {v: k for (k, v) in open_brackets.items()}
    for bracket in brackets:
        if bracket in open_brackets:
            stack.append(bracket)
        elif bracket in close_brackets:
            if not stack or open_brackets[stack.pop()] != bracket:
                return False
    return not stack