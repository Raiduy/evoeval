
def exchange(lst1, lst2):
    lst1_odd = [x for x in lst1 if x % 2 != 0]
    lst2_even = [x for x in lst2 if x % 2 == 0]
    if len(lst1_odd) <= len(lst2_even):
        return "YES"
    else:
        return "NO"
