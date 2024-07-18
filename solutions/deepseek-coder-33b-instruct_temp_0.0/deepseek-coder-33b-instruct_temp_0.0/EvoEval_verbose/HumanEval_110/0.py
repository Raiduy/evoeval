
def exchange(lst1, lst2):
    odd_count_lst1 = sum((i % 2 != 0 for i in lst1))
    odd_count_lst2 = sum((i % 2 != 0 for i in lst2))
    if odd_count_lst1 > odd_count_lst2:
        return 'NO'
    else:
        return 'YES'