def sort_third_modified(l: list, m: list):
    combined = l + m
    third_elements = [combined[i] for i in range(len(combined)) if i % 3 == 0]
    third_elements.sort(reverse=True)
    for i in range(len(combined)):
        if i % 3 == 0:
            combined[i] = third_elements.pop(0)
    return combined