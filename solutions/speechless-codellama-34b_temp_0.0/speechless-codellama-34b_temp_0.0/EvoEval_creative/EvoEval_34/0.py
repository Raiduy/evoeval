def werewolf_transformation(n: int, m: int) -> list:
    transformation_percentages = [0] * n
    for i in range(1, n):
        if i == m:
            transformation_percentages[i] = min(100, transformation_percentages[i - 1] * 2)
        elif i < m:
            transformation_percentages[i] = min(100, transformation_percentages[i - 1] + 10)
        else:
            transformation_percentages[i] = max(0, transformation_percentages[i - 1] - 10)
    return transformation_percentages