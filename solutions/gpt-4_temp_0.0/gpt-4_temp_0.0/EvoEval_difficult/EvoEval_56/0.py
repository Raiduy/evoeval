def correct_bracketing_advanced(brackets: str, scope: tuple):
    stack = []
    pairs = {')': '(', ']': '[', '>': '<', '}': '{'}
    for bracket in brackets:
        if bracket in pairs.values():
            stack.append(bracket)
        elif bracket in pairs.keys():
            if not stack or pairs[bracket] != stack[-1]:
                return False
            else:
                stack.pop()
    return not stack