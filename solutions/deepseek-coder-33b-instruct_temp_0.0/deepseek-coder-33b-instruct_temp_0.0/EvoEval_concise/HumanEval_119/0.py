
def match_parens(lst):
    """
    Accepts a list of two strings composed of open '(' and close ')' parentheses only. 
    Checks whether it's possible to concatenate the strings into a valid sequence where all parentheses are balanced.
    A balanced sequence is one like '(())()', not like '())'.
    Returns 'Yes' if it can create a balanced string, 'No' if it can't.

    Examples:
    match_parens(['()(', ')']) == 'Yes'
    match_parens([')', ')']) == 'No'
    """
    s = lst[0] + lst[1]
    stack = []
    for c in s:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return 'No'
            else:
                stack.pop()
    if len(stack) == 0:
        return 'Yes'
    else:
        return 'No'