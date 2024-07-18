from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """
    # Create an empty set to store unique elements
    unique_numbers = set()
    # Create a new list to store the result
    result = []
    # Iterate over the input list
    for number in numbers:
        # Check if the number is already in the set
        if number not in unique_numbers:
            # If not, add it to the set and the result list
            unique_numbers.add(number)
            result.append(number)
    # Return the result list
    return result
