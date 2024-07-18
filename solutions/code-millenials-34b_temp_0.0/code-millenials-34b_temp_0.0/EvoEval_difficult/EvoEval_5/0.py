from typing import List, Union

def intersperse(numbers: List[Union[int, float]], delimeter: Union[int, float], limit: int) -> List[Union[int, float]]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            if i < limit:
                result.append(delimeter)
    return result