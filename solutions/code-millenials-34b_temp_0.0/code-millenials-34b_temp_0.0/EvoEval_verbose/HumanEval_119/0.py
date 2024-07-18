
def match_parens(lst):
    (s1, s2) = lst
    if s1.count('(') == s1.count(')'):
        if s2.count('(') == s2.count(')'):
            return 'Yes'
        else:
            return 'No'
    else:
        return 'No'