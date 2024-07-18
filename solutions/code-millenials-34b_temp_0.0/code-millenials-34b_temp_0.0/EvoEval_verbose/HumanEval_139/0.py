
def special_factorial(n):
    if n < 0:
        raise ValueError('Input should be a non-negative integer.')
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(n, 0, -1):
            result *= factorial(i)
        return result