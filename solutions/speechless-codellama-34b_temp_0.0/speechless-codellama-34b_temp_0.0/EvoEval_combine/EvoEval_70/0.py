
from typing import List, Tuple
import math


def closest_special_factorial(numbers: List[int]) -> Tuple[int, int]:
    """
    This function will receive a list of integers as input and should return a tuple of two integers 
    that have the closest special factorials. The special factorial is defined as:
    special_factorial(n) = n! * (n-1)! * ... * 1! where n > 0

    The function should return the two numbers whose special factorials are the closest to each other. 
    The result should be in ascending order.
    """
    special_factorials = [special_factorial(n) for n in numbers]
    closest_pair = (numbers[0], numbers[1])
    min_difference = abs(special_factorials[0] - special_factorials[1])
    for i in range(len(special_factorials)):
        for j in range(i + 1, len(special_factorials)):
            difference = abs(special_factorials[i] - special_factorials[j])
            if difference < min_difference:
                min_difference = difference
                closest_pair = (numbers[i], numbers[j])
    return tuple(sorted(closest_pair))