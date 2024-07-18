def is_happy_advanced(s, n):
    if not re.search('[a-zA-Z0-9]', s):
        return False
    if len(s) < n:
        return False
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) < n:
            return False
    return True