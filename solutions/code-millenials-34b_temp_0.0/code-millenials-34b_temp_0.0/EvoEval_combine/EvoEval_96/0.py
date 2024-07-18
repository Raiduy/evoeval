
def common_pairs_with_zero_sum(l1: list, l2: list) -> bool:
    common_elements = set(l1) & set(l2)
    for i in common_elements:
        for j in common_elements:
            if i != j and i + j == 0:
                return True
    return False