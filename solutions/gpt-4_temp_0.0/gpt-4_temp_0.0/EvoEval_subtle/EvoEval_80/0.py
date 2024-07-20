
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 4 and every 4 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adbc) => True
    is_happy(xyyx) => False
    """
    if len(s) < 4:
        return False
    for i in range(len(s) - 3):
        if len(set(s[i:i + 4])) != 4:
            return False
    return True