from typing import List

def validate_input(input: List[int]) -> bool:
    """ Validates if the list contains integer values only.
    Returns True if the input list contains integer values only, otherwise returns False.
    
    >>> validate_input([1, 2, "a", 4])
    False
    >>> validate_input([1, 2, 3, 4])
    True
    """
    for item in input:
        if not isinstance(item, int):
            return False
    return True
from typing import List

def rearrange(numbers: List[int]) -> List[int]:
    """ Rearrange the elements in the given list `numbers' to have all even numbers first, 
    followed by all odd numbers. Keep the order within odd or even numbers the same
    
    The function should return the rearranged list. If the input list contains non-integer values,
    the function should return an empty list.
    
    >>> rearrange([1, 2, 3, 4])
    [2, 4, 1, 3]
    >>> rearrange([1, 2, "a", 4])
    []
    """
    if not validate_input(numbers):
        return []
    even_numbers = []
    odd_numbers = []
    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)
        else:
            odd_numbers.append(num)
    return even_numbers + odd_numbers