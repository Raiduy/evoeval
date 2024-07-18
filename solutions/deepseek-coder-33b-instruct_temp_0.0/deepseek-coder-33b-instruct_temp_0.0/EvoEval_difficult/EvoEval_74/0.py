def total_match(lst1, lst2, k):

    def count_chars(lst):
        return sum((len(s) for s in lst))

    def count_strings(lst, k):
        return sum((1 for s in lst if len(s) <= k))
    if not lst1:
        return lst1
    if not lst2:
        return lst2
    (total1, total2) = (count_chars(lst1), count_chars(lst2))
    (count1, count2) = (count_strings(lst1, k), count_strings(lst2, k))
    if total1 < total2:
        return lst1
    elif total2 < total1:
        return lst2
    elif count1 > count2:
        return lst1
    elif count2 > count1:
        return lst2
    else:
        return lst1