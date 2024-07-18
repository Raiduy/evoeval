def werewolf_transformation(n: int, m: int):
    transformation = [0]
    current_percentage = 0
    for day in range(1, n):
        if day < m:
            current_percentage = min(current_percentage + 10, 100)
        elif day == m:
            current_percentage = min(current_percentage * 2, 100)
        else:
            current_percentage = max(current_percentage - 10, 0)
        transformation.append(current_percentage)
    return transformation