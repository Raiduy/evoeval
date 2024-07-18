def total_match(lst1, lst2, k):
    if not lst1 or not lst2:
        return lst1 or lst2
    total_chars_lst1 = sum((len(s) for s in lst1))
    total_chars_lst2 = sum((len(s) for s in lst2))
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst2 < total_chars_lst1:
        return lst2
    else:
        count_lst1 = sum((1 for s in lst1 if len(s) <= k))
        count_lst2 = sum((1 for s in lst2 if len(s) <= k))
        if count_lst1 > count_lst2:
            return lst1
        else:
            return lst2