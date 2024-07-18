

def correct_bracketing(brackets: str) -> bool:
    open_bracket_count = 0
    for bracket in brackets:
        if bracket == '<':
            open_bracket_count += 1
        elif bracket == '>':
            open_bracket_count -= 1
            if open_bracket_count < 0:
                return False
    return open_bracket_count == 0