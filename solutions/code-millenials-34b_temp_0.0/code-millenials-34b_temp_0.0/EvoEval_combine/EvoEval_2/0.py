
from typing import List

def modp_intersperse(numbers: List[int], n: int, p: int) -> List[int]:
    result = []
    for num in numbers:
        result += [num, pow(2, n, p)]
    return result[:-1]