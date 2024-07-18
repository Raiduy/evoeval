
def strange_sort_list(lst):
    lst.sort()
    result = []
    while lst:
        result.append(lst.pop())
        if lst:
            result.append(lst.pop(0))
    return result