def monotonic_sublist(l: list, k: int):
    for i in range(len(l) - k + 1):
        sublist = l[i:i + k]
        if all((sublist[j] < sublist[j + 1] for j in range(k - 1))) or all((sublist[j] > sublist[j + 1] for j in range(k - 1))):
            return True
    return False