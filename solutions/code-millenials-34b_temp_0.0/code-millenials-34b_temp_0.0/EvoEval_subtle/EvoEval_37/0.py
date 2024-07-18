

def sort_even(l: list):
    even_indices_elements = sorted([l[i] for i in range(0, len(l), 2)], reverse=True)
    for i in range(0, len(l), 2):
        l[i] = even_indices_elements[i // 2]
    return l