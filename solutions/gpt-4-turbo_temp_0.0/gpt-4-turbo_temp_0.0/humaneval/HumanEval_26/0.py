from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Count occurrences of each number
    counts = {}
    for number in numbers:
        counts[number] = counts.get(number, 0) + 1
    
    # Filter numbers that occur more than once
    return [number for number in numbers if counts[number] == 1]
