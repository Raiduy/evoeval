
def special_stone_factorial(n):
    result = []
    for i in range(n, 0, -1):
        factorial = 1
        for j in range(i, 0, -1):
            factorial *= j
        result.append(factorial)
    return result