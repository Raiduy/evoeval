

def correct_bracketing(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>' and (not stack):
            return False
        elif bracket == '>' and stack:
            stack.pop()
    return not stack