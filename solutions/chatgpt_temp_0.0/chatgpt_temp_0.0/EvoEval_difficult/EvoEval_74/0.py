def total_match(lst1, lst2, k):

    def total_chars(lst):
        return sum((len(s) for s in lst))

    def count_strings_less_than_k(lst, k):
        return sum((1 for s in lst if len(s) <= k))
    if not lst1:
        return lst1
    if not lst2:
        return lst2
    total_chars_lst1 = total_chars(lst1)
    total_chars_lst2 = total_chars(lst2)
    count_lst1 = count_strings_less_than_k(lst1, k)
    count_lst2 = count_strings_less_than_k(lst2, k)
    if total_chars_lst1 < total_chars_lst2:
        return lst1
    elif total_chars_lst1 > total_chars_lst2:
        return lst2
    elif count_lst1 > count_lst2:
        return lst1
    elif count_lst1 < count_lst2:
        return lst2
    else:
        return lst1