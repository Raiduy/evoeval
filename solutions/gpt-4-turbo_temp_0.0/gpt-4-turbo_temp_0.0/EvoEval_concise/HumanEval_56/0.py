

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
    counter = 0
    for bracket in brackets:
        if bracket == '<':
            counter += 1
        elif bracket == '>':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0