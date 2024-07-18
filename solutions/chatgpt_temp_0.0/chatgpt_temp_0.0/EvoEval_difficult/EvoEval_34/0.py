def unique(l: list, from_index: int, to_index: int):
    if from_index < 0 or to_index >= len(l):
        return 'Invalid range'
    sub_list = l[from_index:to_index + 1]
    unique_elements = []
    for element in sub_list:
        if element not in unique_elements:
            unique_elements.append(element)
    sorted_unique_elements = sorted(unique_elements)
    return sorted_unique_elements