
import math

def special_brazilian_balloon(n, w):
    brazilian_factorial = math.factorial(n)
    for i in range(1, n):
        brazilian_factorial *= math.factorial(n - i)
    if sum(w) > brazilian_factorial:
        return False
    if w != w[::-1]:
        return False
    return True