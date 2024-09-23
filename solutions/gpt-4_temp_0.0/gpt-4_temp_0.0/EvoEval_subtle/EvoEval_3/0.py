
from typing import List


def below_one(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    one balance. Your task is to detect if at any point the balance of account falls below one, and
    at that point function should return True. Otherwise it should return False.
    >>> below_one([1, 2, 3])
    False
    >>> below_one([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 1:
            return True
    return False