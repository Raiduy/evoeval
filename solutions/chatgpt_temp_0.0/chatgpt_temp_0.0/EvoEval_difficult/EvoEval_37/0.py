def sort_even_odd(l: list, m: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    sorted_even_values = [value for value in m if value in l and value in m] + [value for value in l if value not in m]
    for (i, value) in zip(even_indices, sorted_even_values):
        l[i] = value
    return l