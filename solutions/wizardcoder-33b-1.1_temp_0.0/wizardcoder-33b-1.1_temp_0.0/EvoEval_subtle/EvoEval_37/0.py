

def sort_even(l: list):
    even_indices = [l[i] for i in range(0, len(l), 2)]
    even_indices.sort(reverse=True)
    for i in range(0, len(l), 2):
        l[i] = even_indices[i // 2]
    return l