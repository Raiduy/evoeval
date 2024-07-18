def sort_even_odd(l: list, m: list):
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    even_values = [l[i] for i in even_indices]
    sorted_even_values = []
    for value in m:
        if value in even_values:
            sorted_even_values.append(value)
            even_values.remove(value)
    sorted_even_values.extend(even_values)
    result = l.copy()
    for (i, value) in enumerate(result):
        if i % 2 == 0:
            result[i] = sorted_even_values.pop(0)
    return result