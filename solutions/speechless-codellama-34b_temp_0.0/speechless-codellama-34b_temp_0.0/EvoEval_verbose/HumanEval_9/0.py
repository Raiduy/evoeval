from typing import List, Tuple


def rolling_max(numbers: List[int]) -> List[int]:
    max_list = []
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        max_list.append(max_num)
    return max_list