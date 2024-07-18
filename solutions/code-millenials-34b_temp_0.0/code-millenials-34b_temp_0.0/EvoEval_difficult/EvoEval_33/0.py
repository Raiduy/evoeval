def sort_third_modified(l: list, m: list):
    concat = l + m
    third_indices_values = [concat[i] for i in range(len(concat)) if i % 3 == 0]
    third_indices_values.sort(reverse=True)
    new_list = l.copy()
    for i in range(len(new_list)):
        if i % 3 == 0:
            new_list[i] = third_indices_values.pop(0)
    if m:
        new_list += m
    return new_list