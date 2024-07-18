
def total_match(lst1, lst2):
    total_count_lst1 = sum((len(s) for s in lst1))
    total_count_lst2 = sum((len(s) for s in lst2))
    if total_count_lst1 < total_count_lst2:
        return lst1
    elif total_count_lst1 > total_count_lst2:
        return lst2
    else:
        return lst1