def get_digit_count(n: int) -> int:
    return len(str(n))
from typing import List, Tuple

def distribute_candies(candies: List[int], n: int) -> List[int]:
    result = [0] * n
    i = 0
    while candies:
        for j in range(n):
            if not candies:
                break
            count = get_digit_count(i + 1)
            if candies[0] >= count:
                result[j] += count
                candies[0] -= count
                if candies[0] == 0:
                    candies.pop(0)
            else:
                result[j] += candies[0]
                candies[0] = 0
        i += 1
    return result