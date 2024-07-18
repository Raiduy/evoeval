from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for i in numbers:
        result += [i, delimeter]
    return result[:-1]  # We trim the last inserted delimeter

