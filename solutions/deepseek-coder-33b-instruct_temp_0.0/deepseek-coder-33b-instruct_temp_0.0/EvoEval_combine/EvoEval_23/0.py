
def special_stone_factorial(n):

    def factorial(n):
        if n == 0 or n == 1:
            return 1
        else:
            return n * factorial(n - 1)

    def brazilian_factorial(n):
        result = 1
        for i in range(1, n + 1):
            result *= factorial(i)
        return result
    result = []
    for i in range(n):
        if n % 2 == 0:
            n += 1
        else:
            n += 2
        result.append(brazilian_factorial(n))
    return result