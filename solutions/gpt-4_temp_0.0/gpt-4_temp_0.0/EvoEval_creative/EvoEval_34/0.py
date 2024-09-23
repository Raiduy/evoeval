def werewolf_transformation(n: int, m: int):
    transformation = [0]
    for i in range(1, n):
        if i < m:
            transformation.append(min(transformation[-1] + 10, 100))
        elif i == m:
            transformation.append(min(transformation[-1] * 2, 100))
        else:
            transformation.append(max(transformation[-1] - 10, 0))
    return transformation