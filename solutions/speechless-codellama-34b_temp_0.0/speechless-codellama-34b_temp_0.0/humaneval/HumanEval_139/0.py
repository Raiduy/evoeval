
def special_factorial(n):
    if n == 0:
        return 1
    else:
        factorial = 1
        for i in range(n, 0, -1):
            factorial *= i
        return factorial
