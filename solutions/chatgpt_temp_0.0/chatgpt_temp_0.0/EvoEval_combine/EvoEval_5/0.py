
from typing import List

def sort_and_check(numbers: List[float], threshold: float) -> List[float]:
    """
    Given an array of numbers, check if any two numbers in the array are closer to each other 
    than the given threshold. If yes, sort the array according to the following rules:

    - If the sum of the first and last numbers in the array is even, sort the array in descending order.
    - If the sum of the first and last numbers in the array is odd, sort the array in ascending order.
    
    If no two numbers are closer than the threshold, return the array as it is.
    
    Note: Consider the sum as even or odd after rounding off to the nearest integer.

    Examples:
    * sort_and_check([1.0, 2.0, 3.0], 0.5) => [1.0, 2.0, 3.0]
    * sort_and_check([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3) => [1.0, 2.0, 2.8, 3.0, 4.0, 5.0]
    * sort_and_check([4.0, 2.0, 3.0, 0.0], 2.0) => [4.0, 3.0, 2.0, 0.0]
    """
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                if round(numbers[0] + numbers[-1]) % 2 == 0:
                    numbers.sort(reverse=True)
                else:
                    numbers.sort()
                return numbers
    return numbers