def max_element_diff(l: list, n: int):
    if n > len(l):
        return None
    else:
        max_element = max(l)
        nth_max_element = sorted(set(l), reverse=True)[n - 1]
        return (nth_max_element, max_element - nth_max_element)