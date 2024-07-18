

def correct_bracketing(brackets: str):
    """
    Checks if each '<' has a matching '>' in the string.
    Assumes string consists only of '<' and '>' characters.

    >>> correct_bracketing("<")
    False
    >>> correct_bracketing("<>")
    True
    >>> correct_bracketing("<<><>>")
    True
    >>> correct_bracketing("><<>")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == '<':
            stack.append(bracket)
        elif bracket == '>':
            if len(stack) == 0:
                return False
            stack.pop()
    return len(stack) == 0