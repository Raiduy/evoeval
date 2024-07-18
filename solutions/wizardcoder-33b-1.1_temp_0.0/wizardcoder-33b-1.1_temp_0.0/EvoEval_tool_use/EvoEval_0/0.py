def get_digit_count(n: int) -> int:
    return len(str(n))
from typing import List, Tuple

def distribute_candies(candies: List[int], n: int) -> List[int]:
    child_candies = [0] * n
    i = 0
    while candies:
        candy = candies.pop(0)
        while candy > 0:
            if candy >= get_digit_count(i + 1):
                child_candies[i % n] += get_digit_count(i + 1)
                candy -= get_digit_count(i + 1)
            else:
                child_candies[i % n] += candy
                candy = 0
            i += 1
    return child_candies