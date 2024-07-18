
def match_parens(lst):
    s = ''.join(lst)
    count = 0
    for char in s:
        if char == '(':
            count += 1
        elif char == ')':
            count -= 1
            if count < 0:
                return 'No'
    return 'Yes' if count == 0 else 'No'