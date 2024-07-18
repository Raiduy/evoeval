
def match_parens(lst):
    lst1, lst2 = lst

    open_count_1 = lst1.count('(')
    close_count_1 = lst1.count(')')

    open_count_2 = lst2.count('(')
    close_count_2 = lst2.count(')')

    if open_count_1 < close_count_1 and open_count_2 > close_count_2:
        return 'Yes'
    elif open_count_1 > close_count_1 and open_count_2 < close_count_2:
        return 'Yes'
    elif open_count_1 == close_count_1 and open_count_1 + open_count_2 == close_count_1 + close_count_2:
        return 'Yes'
    else:
        return 'No'
