from typing import List, Optional

def rescale_to_unit(numbers: List[Optional[float]]) -> List[Optional[float]]:
    non_none_numbers = [num for num in numbers if num is not None]
    min_num = min(non_none_numbers)
    max_num = max(non_none_numbers)
    range_num = max_num - min_num
    rescaled_numbers = [round((num - min_num) / range_num, 2) if num is not None else None for num in numbers]
    return rescaled_numbers