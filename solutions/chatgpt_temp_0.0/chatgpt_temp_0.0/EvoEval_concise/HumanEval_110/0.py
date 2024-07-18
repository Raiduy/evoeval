
def exchange(lst1, lst2):
    if all((num % 2 == 0 for num in lst1)):
        return 'YES'
    odd_count_lst1 = sum((num % 2 != 0 for num in lst1))
    odd_count_lst2 = sum((num % 2 != 0 for num in lst2))
    if odd_count_lst1 >= odd_count_lst2:
        return 'YES'
    else:
        return 'NO'