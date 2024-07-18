
def strange_sort_list(lst):
    lst.sort()
    result = []
    pop_from_end = False
    while lst:
        if pop_from_end:
            result.append(lst.pop())
        else:
            result.append(lst.pop(0))
        pop_from_end = not pop_from_end
    return result