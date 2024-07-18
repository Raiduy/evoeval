

def sort_even(l: list):
    even_indices = [l[i] for i in range(0, len(l), 2)]
    even_indices.sort()
    for i in range(0, len(l), 2):
        l[i] = even_indices.pop(0)
    return l