def same_chars_in_order(s0: str, s1: str) -> bool:
    i = j = 0
    while i < len(s0) and j < len(s1):
        if s0[i] == s1[j]:
            i += 1
        j += 1
    return i == len(s0)