from typing import List, Union

def intersperse(numbers: List[Union[int, float]], delimeter: Union[int, float], limit: int) -> List[Union[int, float]]:
    result = []
    for (i, number) in enumerate(numbers):
        result.append(number)
        if i < len(numbers) - 1 and i < limit:
            result.append(delimeter)
    return result