
import math

def special_brazilian_balloon(n, w):

    def brazilian_factorial(n):
        if n == 0:
            return 1
        else:
            return n * brazilian_factorial(n - 1)
    max_weight = brazilian_factorial(n)
    total_weight = sum(w)
    if total_weight > max_weight:
        return False
    if w != w[::-1]:
        return False
    return True