
from typing import List

def modp_intersperse(numbers: List[int], n: int, p: int) -> List[int]:
    result = []
    for i in range(len(numbers)):
        result.append(numbers[i])
        if i < len(numbers) - 1:
            result.append(2 ** n % p)
    return result