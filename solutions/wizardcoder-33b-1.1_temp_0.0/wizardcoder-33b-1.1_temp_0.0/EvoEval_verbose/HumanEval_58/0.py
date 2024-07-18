

def common(l1: list, l2: list):
    set1 = set(l1)
    set2 = set(l2)
    common_elements = set1 & set2
    sorted_common_elements = sorted(list(common_elements))
    return sorted_common_elements