
def total_match(lst1, lst2):
    total_lst1 = sum((len(s) for s in lst1))
    total_lst2 = sum((len(s) for s in lst2))
    if total_lst1 <= total_lst2:
        return lst1
    else:
        return lst2