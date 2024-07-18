
def match_parens(lst):
    str1 = lst[0] + lst[1]
    str2 = lst[1] + lst[0]
    if is_good_string(str1) or is_good_string(str2):
        return 'Yes'
    else:
        return 'No'