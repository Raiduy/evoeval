
def exchange(lst1, lst2):
    """
    This function checks if it's possible to swap elements between lst1 and lst2
    to make all elements in lst1 even.
    """
    even_in_lst1 = sum((1 for x in lst1 if x % 2 == 0))
    even_in_lst2 = sum((1 for x in lst2 if x % 2 == 0))
    odd_in_lst1 = len(lst1) - even_in_lst1
    if odd_in_lst1 <= even_in_lst2:
        return 'YES'
    else:
        return 'NO'