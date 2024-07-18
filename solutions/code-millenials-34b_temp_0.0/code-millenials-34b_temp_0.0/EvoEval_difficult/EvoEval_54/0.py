def same_chars_in_order(s0: str, s1: str) -> bool:
    """
    Check if characters in s0 appears in the same order in s1.
    """
    s0_index = 0
    for char in s1:
        if s0_index == len(s0):
            break
        if char == s0[s0_index]:
            s0_index += 1
    return s0_index == len(s0)