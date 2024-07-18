def werewolf_transformation(n: int, m: int):
    transformation_percentages = [0]
    for i in range(1, n):
        if i < m:
            transformation_percentages.append(min(100, transformation_percentages[i - 1] + 10))
        elif i == m:
            transformation_percentages.append(min(100, transformation_percentages[i - 1] * 2))
        else:
            transformation_percentages.append(max(0, transformation_percentages[i - 1] - 10))
    return transformation_percentages