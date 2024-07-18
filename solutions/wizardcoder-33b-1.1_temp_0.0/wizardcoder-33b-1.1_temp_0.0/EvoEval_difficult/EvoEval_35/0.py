def max_element_diff(l: list, n: int):
    if n > len(l):
        return None
    else:
        l.sort(reverse=True)
        nth_max = l[n - 1]
        diff = l[0] - nth_max
        return (nth_max, diff)