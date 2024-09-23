def sort_even_odd(l: list, m: list):
    even_indices = [l[i] for i in range(len(l)) if i % 2 == 0]
    sorted_even_indices = [x for x in m if x in even_indices]
    not_in_m = [x for x in even_indices if x not in m]
    sorted_even_indices.extend(not_in_m)
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(sorted_even_indices.pop(0))
        else:
            result.append(l[i])
    return result