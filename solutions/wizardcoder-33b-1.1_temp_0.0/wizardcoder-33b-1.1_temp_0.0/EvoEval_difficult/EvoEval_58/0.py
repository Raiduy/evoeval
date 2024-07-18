def common(l1: list, l2: list, n: int):
    common_strings = [value for value in l1 if value in l2]
    common_strings.sort(key=lambda x: (-len(x), l1.index(x)))
    return common_strings[:n]