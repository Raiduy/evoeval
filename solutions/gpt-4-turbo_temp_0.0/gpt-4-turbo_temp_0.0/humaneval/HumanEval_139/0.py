
def special_factorial(n):
    """Calculate the Brazilian factorial of n."""
    result = 1
    for i in range(1, n + 1):
        result *= factorial(i)
    return result
