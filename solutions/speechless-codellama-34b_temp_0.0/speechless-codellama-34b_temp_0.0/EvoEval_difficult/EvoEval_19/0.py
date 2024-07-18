from typing import List, Tuple


def sort_numbers(numbers: str, order: List[str]) -> str:
    num_list = numbers.split()
    order_dict = {num: i for (i, num) in enumerate(order)}
    sorted_nums = sorted(num_list, key=lambda x: order_dict.get(x, len(order_dict)))
    return ' '.join(sorted_nums)