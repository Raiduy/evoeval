def get_digit_count(n: int) -> int:
    return len(str(n))
from typing import List, Tuple

def distribute_candies(candies: List[int], n: int) -> List[int]:
    result = [0] * n
    remaining_candies = sum(candies)
    while remaining_candies > 0:
        for i in range(n):
            if remaining_candies >= get_digit_count(i + 1):
                result[i] += get_digit_count(i + 1)
                remaining_candies -= get_digit_count(i + 1)
            else:
                result[i] += remaining_candies
                remaining_candies = 0
                break
    return result