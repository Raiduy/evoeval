def unique(l: list, from_index: int, to_index: int):
    if from_index < 0 or to_index >= len(l) or from_index > to_index:
        return 'Invalid range'
    unique_list = []
    for i in range(from_index, to_index + 1):
        if l[i] not in unique_list:
            unique_list.append(l[i])
    for i in range(len(unique_list)):
        for j in range(i + 1, len(unique_list)):
            if unique_list[i] > unique_list[j]:
                (unique_list[i], unique_list[j]) = (unique_list[j], unique_list[i])
    return unique_list