
def total_match(lst1, lst2):
    count_lst1 = sum((len(s) for s in lst1))
    count_lst2 = sum((len(s) for s in lst2))
    if count_lst1 <= count_lst2:
        return lst1
    else:
        return lst2