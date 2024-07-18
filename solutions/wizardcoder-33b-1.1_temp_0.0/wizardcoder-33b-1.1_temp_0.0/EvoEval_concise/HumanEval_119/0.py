
def match_parens(lst):
    s = lst[0] + lst[1]
    count = 0
    for c in s:
        if c == '(':
            count += 1
        elif c == ')':
            count -= 1
        if count < 0:
            return 'No'
    if count != 0:
        return 'No'
    return 'Yes'