
def sum_square_cube_to_n(n: int):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0:
            result.append(i ** 2)
        elif i % 4 == 0:
            result.append(i ** 3)
        else:
            result.append(i)
    return sum(result)