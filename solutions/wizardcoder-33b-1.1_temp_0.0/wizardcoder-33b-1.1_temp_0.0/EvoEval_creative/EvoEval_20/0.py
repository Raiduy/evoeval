def generate_pattern(n: int):
    if n <= 0:
        return []
    pattern = []
    for i in range(1, n + 1):
        pattern.append(','.join(map(str, list(range(1, i + 1)))))
        pattern.append(','.join(map(str, list(range(i, 0, -1)))))
    return pattern