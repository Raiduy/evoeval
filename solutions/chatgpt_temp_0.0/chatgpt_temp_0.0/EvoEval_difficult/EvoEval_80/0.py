def is_happy_advanced(s, n):
    if len(s) < n:
        return False
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(set(substring)) != n or not any((c.isalnum() for c in substring)):
            return False
    return True