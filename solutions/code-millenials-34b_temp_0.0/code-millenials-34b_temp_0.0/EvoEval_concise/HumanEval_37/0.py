

def sort_even(l: list):
    even_list = [l[i] for i in range(0, len(l), 2)]
    even_list.sort()
    new_l = l.copy()
    for i in range(0, len(l), 2):
        new_l[i] = even_list.pop(0)
    return new_l