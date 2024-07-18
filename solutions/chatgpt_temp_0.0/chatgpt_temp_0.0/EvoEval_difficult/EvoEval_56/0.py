def correct_bracketing_advanced(brackets: str, scope: tuple):
    opening_brackets = scope[0] + scope[1]
    closing_brackets = scope[1] + scope[0]
    stack = []
    for bracket in brackets:
        if bracket in opening_brackets:
            stack.append(bracket)
        elif bracket in closing_brackets:
            if len(stack) == 0:
                return False
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(bracket):
                return False
    return len(stack) == 0