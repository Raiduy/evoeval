
def match_parens(lst):
    if len(lst) != 2:
        return 'No'
    (str1, str2) = lst
    (open1, close1) = (str1.count('('), str1.count(')'))
    (open2, close2) = (str2.count('('), str2.count(')'))
    if close1 <= open1 and open1 + open2 == close1 + close2:
        return 'Yes'
    if close2 <= open2 and open1 + open2 == close1 + close2:
        return 'Yes'
    return 'No'