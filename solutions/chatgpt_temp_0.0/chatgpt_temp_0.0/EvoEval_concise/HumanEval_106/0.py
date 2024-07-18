
def f(n):
    """
    Implement a function f, taking n as an input and returning a list of size n. For each index i, the value is i's factorial for even i or the sum of numbers up to i for odd i. i starts from 1. Factorial is the product of numbers from 1 to i. 
    Example: 
    f(5) == [1, 2, 6, 24, 15]  
    """
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            factorial = 1
            for j in range(1, i + 1):
                factorial *= j
            result.append(factorial)
        else:
            total = 0
            for j in range(1, i + 1):
                total += j
            result.append(total)
    return result