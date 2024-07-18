def correct_bracketing_advanced(brackets: str):
    stack = []
    for bracket in brackets:
        if bracket in '([{':
            stack.append(bracket)
        elif bracket in ')]}':
            if not stack:
                return False
            if bracket == ')' and stack[-1] != '(':
                return False
            if bracket == ']' and stack[-1] != '[':
                return False
            if bracket == '}' and stack[-1] != '{':
                return False
            stack.pop()
    return not stack