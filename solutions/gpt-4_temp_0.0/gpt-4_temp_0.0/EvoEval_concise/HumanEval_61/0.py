

def correct_bracketing(brackets: str):
    """ 
    Checks if every opening bracket in the input string 'brackets' has a corresponding closing bracket. 
    Returns True if so, otherwise False.

    >>> correct_bracketing("(")
    False
    >>> correct_bracketing("()")
    True
    >>> correct_bracketing("(()())")
    True
    >>> correct_bracketing(")(()")
    False
    """
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif bracket == ')':
            if not stack:
                return False
            stack.pop()
    return len(stack) == 0