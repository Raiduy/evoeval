
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
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            special_factorial_i = factorial(numbers[i])
            special_factorial_j = factorial(numbers[j])
            if abs(special_factorial_i - special_factorial_j) <= threshold:
                return True
    return False