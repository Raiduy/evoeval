

def sort_even(l: list):
    even_list = sorted(l[::2])
    for i in range(0, len(l), 2):
        l[i] = even_list.pop(0)
    return l
