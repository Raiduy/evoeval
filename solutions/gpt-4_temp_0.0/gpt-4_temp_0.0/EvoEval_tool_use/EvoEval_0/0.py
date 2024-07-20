def get_digit_count(n: int) -> int:
    return len(str(n))
from typing import List, Tuple

def distribute_candies(candies: List[int], n: int) -> List[int]:
    children = [0] * n
    child = 0
    while candies:
        candy = candies.pop(0)
        while candy > 0:
            digit_count = get_digit_count(child + 1)
            if candy >= digit_count:
                children[child] += digit_count
                candy -= digit_count
            else:
                children[child] += candy
                candy = 0
            child = (child + 1) % n
    return children