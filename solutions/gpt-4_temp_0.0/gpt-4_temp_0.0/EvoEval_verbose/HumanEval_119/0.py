
def match_parens(lst):
    (str1, str2) = (lst[0], lst[1])
    if str1[0] == ')' or str2[-1] == '(':
        return 'No'
    if str1.count('(') <= str2.count(')'):
        return 'Yes'
    return 'No'