def generate_pattern(n: int):
    if n <= 0:
        return []
    patterns = []
    for i in range(1, n + 1):
        pattern = ','.join((str(j) for j in range(1, i + 1)))
        patterns.append(pattern)
    for i in range(n, 0, -1):
        pattern = ','.join((str(j) for j in range(1, i + 1)))
        patterns.append(pattern)
    return patterns