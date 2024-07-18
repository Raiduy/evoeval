
def match_parens(lst):
    str1 = lst[0] + lst[1]
    str2 = lst[1] + lst[0]
    open_count = 0
    close_count = 0
    for char in str1:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        if close_count > open_count:
            return 'No'
    open_count = 0
    close_count = 0
    for char in str2:
        if char == '(':
            open_count += 1
        elif char == ')':
            close_count += 1
        if close_count > open_count:
            return 'No'
    return 'Yes'