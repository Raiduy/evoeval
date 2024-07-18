
def exchange(lst1, lst2):
    odd_in_lst1 = sum((1 for i in lst1 if i % 2 != 0))
    odd_in_lst2 = sum((1 for i in lst2 if i % 2 != 0))
    if odd_in_lst1 > odd_in_lst2:
        return 'NO'
    else:
        return 'YES'