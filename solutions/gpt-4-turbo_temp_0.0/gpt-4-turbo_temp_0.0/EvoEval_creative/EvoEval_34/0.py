def werewolf_transformation(n: int, m: int):
    transformation_percentages = [0]
    for day in range(2, n + 1):
        if day < m:
            transformation_percentages.append(min(transformation_percentages[-1] + 10, 100))
        elif day == m:
            transformation_percentages.append(min(transformation_percentages[-1] * 2, 100))
        else:
            transformation_percentages.append(max(transformation_percentages[-1] - 10, 0))
    return transformation_percentages