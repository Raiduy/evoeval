def monotonic_sublist(l: list, k: int):
    for i in range(len(l) - k + 1):
        sublist = l[i:i + k]
        if sublist == sorted(sublist) or sublist == sorted(sublist, reverse=True):
            return True
    return False