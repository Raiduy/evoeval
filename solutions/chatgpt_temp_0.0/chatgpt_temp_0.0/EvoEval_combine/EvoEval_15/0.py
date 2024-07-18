from typing import List

def balance_triples(operations: List[int]) -> bool:
    """
    balance_triples takes a list of deposit and withdrawal operations on a bank account that starts with
    zero balance. It returns True if there are at least three distinct points in time where the balance of account sums to zero (excluding the initial balance), 
    and False otherwise. If at any point the balance of account falls below zero, function should immediately return False.
    
    >>> balance_triples([1, -1, 2, -2, 3, -3])
    True
    >>> balance_triples([1, 2, 3, -6])
    False
    >>> balance_triples([1, 2, -4, 5])
    False
    >>> balance_triples([2, -2, 3, -3, 4, -4])
    True
    >>> balance_triples([1, -1, 2])
    False
    """
    balance = 0
    zero_sums = set()
    for i in range(len(operations)):
        balance += operations[i]
        if balance < 0:
            return False
        if balance == 0:
            zero_sums.add(i)
    return len(zero_sums) >= 3