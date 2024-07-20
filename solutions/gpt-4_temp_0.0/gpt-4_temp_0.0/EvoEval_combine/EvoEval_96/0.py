
def common_pairs_with_zero_sum(l1: list, l2: list) -> bool:
    common_elements = set(l1) & set(l2)
    for element in common_elements:
        if -element in common_elements and element != -element:
            return True
    return False