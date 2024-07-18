def common(l1: list, l2: list, n: int):
    common_words = [value for value in l1 if value in l2]
    common_words.sort(key=lambda x: (len(x), l1.index(x)))
    return common_words[:n]