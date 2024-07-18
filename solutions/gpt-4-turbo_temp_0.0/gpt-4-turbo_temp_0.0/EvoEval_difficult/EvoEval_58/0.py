def common(l1: list, l2: list, n: int) -> list:
    """Return the n longest strings, sorted by increasing length that are common in two lists.
       However, in the case of a tie, prioritize the string that appears first in list1.
    """
    common_elements = set(l1) & set(l2)
    sorted_common_elements = sorted(common_elements, key=lambda x: (len(x), l1.index(x)))
    return sorted_common_elements[-n:]