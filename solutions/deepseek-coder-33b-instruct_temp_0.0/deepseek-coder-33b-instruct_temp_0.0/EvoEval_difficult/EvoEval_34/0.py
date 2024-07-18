def unique(l: list, from_index: int, to_index: int):
    if from_index < 0 or to_index >= len(l) or from_index > to_index:
        return 'Invalid range'
    sublist = l[from_index:to_index + 1]
    unique_elements = []
    for i in sublist:
        if i not in unique_elements:
            unique_elements.append(i)
    for i in range(len(unique_elements)):
        for j in range(i + 1, len(unique_elements)):
            if unique_elements[i] > unique_elements[j]:
                (unique_elements[i], unique_elements[j]) = (unique_elements[j], unique_elements[i])
    return unique_elements