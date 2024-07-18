

def common(l1: list, l2: list):
    common_set = set(l1) & set(l2)
    common_list = sorted(list(common_set))
    return common_list