
def sum_square_cube_to_n(n: int) -> int:
    sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            sum += i ** 2
        elif i % 4 == 0:
            sum += i ** 3
        else:
            sum += i
    return sum