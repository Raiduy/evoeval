
def special_stone_factorial(n):
    result = []
    for i in range(n, 0, -1):
        if i % 2 == 0:
            stones = i * 2
        else:
            stones = i * 2 - 1
        factorial = 1
        for j in range(1, stones + 1):
            factorial *= j
        result.append(factorial)
    return result