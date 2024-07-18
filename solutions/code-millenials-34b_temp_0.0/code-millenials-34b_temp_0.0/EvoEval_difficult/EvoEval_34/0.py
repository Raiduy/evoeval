def unique(l: list, from_index: int, to_index: int):
    if from_index < 0 or to_index >= len(l) or from_index > to_index:
        return 'Invalid range'
    sub_list = l[from_index:to_index + 1]
    unique_list = []
    for num in sub_list:
        if num not in unique_list:
            unique_list.append(num)
    unique_list.sort()
    return unique_list