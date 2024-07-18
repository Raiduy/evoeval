def total_match(lst1, lst2, k):
    if len(lst1) == 0:
        return lst2
    if len(lst2) == 0:
        return lst1
    total_chars_lst1 = sum((len(s) for s in lst1))
    total_chars_lst2 = sum((len(s) for s in lst2))
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst1 > total_chars_lst2:
        return lst2
    else:
        len_lst1 = len([s for s in lst1 if len(s) <= k])
        len_lst2 = len([s for s in lst2 if len(s) <= k])
        if len_lst1 > len_lst2:
            return lst1
        elif len_lst2 > len_lst1:
            return lst2
        else:
            return lst1