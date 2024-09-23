
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
    s = ''.join(lst)
    open_parens = 0
    for char in s:
        if char == '(':
            open_parens += 1
        elif char == ')':
            open_parens -= 1
            if open_parens < 0:
                return 'No'
    return 'Yes' if open_parens == 0 else 'No'