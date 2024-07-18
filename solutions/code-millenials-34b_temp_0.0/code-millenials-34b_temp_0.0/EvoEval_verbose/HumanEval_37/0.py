

def sort_even(l: list):
    even_indices_elements = [l[i] for i in range(0, len(l), 2)]
    even_indices_elements.sort()
    sorted_list = l.copy()
    for i in range(0, len(sorted_list), 2):
        sorted_list[i] = even_indices_elements[i // 2]
    return sorted_list