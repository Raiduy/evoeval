def get_digit_count(n: int) -> int:
    return len(str(n))
from typing import List, Tuple

def distribute_candies(candies: List[int], n: int) -> List[int]:
    children_candies = [0] * n
    i = 0
    while candies:
        for j in range(n):
            if candies:
                digit_count = get_digit_count(j + 1)
                while candies and candies[0] <= digit_count:
                    children_candies[j] += candies.pop(0)
                if candies:
                    children_candies[j] += candies.pop(0)
            else:
                break
    return children_candies