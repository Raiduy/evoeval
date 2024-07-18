
def same_chars(s0: str, s1: str) -> bool:
    """
    Check if two words have the same characters and the same length.
    """
    return sorted(s0) == sorted(s1) and len(s0) == len(s1)