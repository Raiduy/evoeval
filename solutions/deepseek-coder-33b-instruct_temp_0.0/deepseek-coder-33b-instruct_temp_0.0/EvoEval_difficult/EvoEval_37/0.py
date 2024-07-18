def sort_even_odd(l: list, m: list):
    sorted_even_indices = []
    for i in m:
        if i in l:
            sorted_even_indices.append(i)
    odd_indices = []
    for i in range(len(l)):
        if i % 2 != 0:
            odd_indices.append(l[i])
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(l[i])
        elif sorted_even_indices:
            result.append(sorted_even_indices.pop(0))
        else:
            result.append(odd_indices.pop(0))
    return result