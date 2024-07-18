
from typing import List
from math import factorial

def special_close_factorials(numbers: List[int], threshold: int) -> bool:
    """ 
    Check if in given list of numbers, are any two special factorials closer to each other than 
    given threshold. The special factorial (Brazilian factorial) is defined as n! * (n-1)! * (n-2)! * ... * 1! 
    where n > 0.

    For example:
    >>> special_close_factorials([2, 3], 10)
    False
    >>> special_close_factorials([1, 2, 3, 4], 100)
    True
    """
    factorials = [factorial(n) for n in numbers]
    factorials.sort()
    for i in range(len(factorials) - 1):
        if factorials[i + 1] - factorials[i] < threshold:
            return True
    return False