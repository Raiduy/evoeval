from typing import List


def below_zero(operations: List[int]) -> bool:
    """ Determine if the account balance drops below zero at any point given a list of deposit and withdrawal operations. 
    The function should return True if it does, otherwise return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for operation in operations:
        balance += operation
        if balance < 0:
            return True
    return False