
from typing import List


def below_one(operations: List[int]) -> bool:
    balance = 1
    for operation in operations:
        balance += operation
        if balance < 1:
            return True
    return False