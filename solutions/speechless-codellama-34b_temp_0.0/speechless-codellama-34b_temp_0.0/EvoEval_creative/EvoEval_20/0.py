def generate_pattern(n: int):
    if n <= 0:
        return []
    else:
        pattern = []
        for i in range(1, n + 1):
            pattern.append(','.join((str(j) for j in range(1, i + 1))))
        for i in range(n - 1, 0, -1):
            pattern.append(','.join((str(j) for j in range(i, 0, -1))))
        return pattern