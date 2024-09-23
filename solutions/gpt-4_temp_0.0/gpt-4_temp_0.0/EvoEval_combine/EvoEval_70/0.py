
from typing import List, Tuple
import math


def closest_special_factorial(numbers: List[int]) -> Tuple[int, int]:
    """Find the two numbers with the closest special factorials."""
    special_factorials = {n: special_factorial(n) for n in numbers}
    sorted_numbers = sorted(special_factorials, key=special_factorials.get)