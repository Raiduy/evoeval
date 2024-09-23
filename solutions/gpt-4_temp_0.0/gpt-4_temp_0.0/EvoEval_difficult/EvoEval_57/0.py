def monotonic_sublist(l: list, k: int) -> bool:
    if len(l) < k:
        return False
    for i in range(len(l) - k + 1):
        sublist = l[i:i + k]
        if all((sublist[i] <= sublist[i + 1] for i in range(len(sublist) - 1))) or all((sublist[i] >= sublist[i + 1] for i in range(len(sublist) - 1))):
            return True
    return False