def is_happy_advanced(s, n):
    if len(s) < n:
        return False
    if not any((c.isalnum() for c in s)):
        return False
    for i in range(len(s) - n + 1):
        if len(set(s[i:i + n])) != n:
            return False
    return True