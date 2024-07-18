
def special_stone_factorial(n):
    levels = []
    for i in range(n, 0, -1):
        if n % 2 == 0:
            levels.append(i * math.factorial(i - 1))
        else:
            levels.append(i * math.factorial(i - 1))
        n -= 1
    return levels[::-1]