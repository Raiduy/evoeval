
def special_factorial(n):
    def factorial(x):
        if x == 0:
            return 1
        else:
            return x * factorial(x - 1)

    result = 1
    for i in range(n, 0, -1):
        result *= factorial(i)

    return result

