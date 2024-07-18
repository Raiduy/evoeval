
import math

def special_brazilian_balloon(n, w):

    def brazilian_factorial(n):
        result = 1
        for i in range(n, 0, -1):
            result *= math.factorial(i)
        return result
    max_weight = brazilian_factorial(n)
    sum_weights = sum(w)
    is_balanced = w == w[::-1]
    return sum_weights <= max_weight and is_balanced