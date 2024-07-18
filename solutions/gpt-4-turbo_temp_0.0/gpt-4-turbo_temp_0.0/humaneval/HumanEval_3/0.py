from typing import List


def below_zero(operations: List[int]) -> bool:
    """ You're given a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. Your task is to detect if at any point the balance of account falls below zero, and
    at that point function should return True. Otherwise it should return False.
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0  # Start with a balance of 0
    for operation in operations:
        balance += operation  # Update the balance with each operation
        if balance < 0:  # Check if the balance falls below zero
            return True  # Return True immediately if the balance is below zero
    return False  # Return False if the balance never falls below zero
