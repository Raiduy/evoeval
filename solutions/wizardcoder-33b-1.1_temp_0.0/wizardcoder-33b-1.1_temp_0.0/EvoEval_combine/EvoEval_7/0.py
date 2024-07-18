
def sum_square_cube_to_n(n: int):
    result = 0
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 4 != 0:
            result += i ** 2
        elif i % 4 == 0:
            result += i ** 3
        else:
            result += i
    return result