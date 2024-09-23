
def f(n):
    """
    Implement a function f, taking n as an input and returning a list of size n. For each index i, the value is i's factorial for even i or the sum of numbers up to i for odd i. i starts from 1. Factorial is the product of numbers from 1 to i. 
    Example: 
    f(5) == [1, 2, 6, 24, 15]  
    """

    def factorial(i):
        if i == 0 or i == 1:
            return 1
        else:
            return i * factorial(i - 1)

    def sum_up_to(i):
        return sum(range(1, i + 1))
    result = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            result.append(factorial(i))
        else:
            result.append(sum_up_to(i))
    return result