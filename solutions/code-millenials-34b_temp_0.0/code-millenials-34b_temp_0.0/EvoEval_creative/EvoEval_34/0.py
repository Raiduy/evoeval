def werewolf_transformation(n: int, m: int):
    percentages = [0] * n
    if m > 0:
        for i in range(1, m):
            percentages[i] = percentages[i - 1] + 10
        percentages[m - 1] = percentages[m - 2] * 2
        for i in range(m, n):
            percentages[i] = max(0, percentages[i - 1] - 10)
    return percentages