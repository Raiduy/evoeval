def sort_even_odd(l: list, m: list):
    even_indices_l = {i: l[i] for i in range(0, len(l), 2)}
    sorted_m = sorted([value for value in m if value in even_indices_l.values()])
    result = l.copy()
    for i in range(0, len(result), 2):
        if result[i] in sorted_m:
            result[i] = sorted_m.pop(0)
    for value in sorted_m:
        for i in range(0, len(result), 2):
            if result[i] == even_indices_l[i] and value in result:
                result[i] = value
                break
    return result