
def next_smallest(lst):
    if len(lst) < 2:
        return None
    else:
        lst.sort()
        smallest = lst[0]
        for i in range(1, len(lst)):
            if lst[i] > smallest:
                return lst[i]
        return None
