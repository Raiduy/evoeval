from typing import List

def teleporter_energy_signature(flux_values: List[int]) -> int:
    """
    In the year 7082, teleporters are the primary mode of transportation across cities. Teleporter do
    not function without a unique energy signature. This unique energy signature is formed by
    performing certain operations over list of flux values recorded daily.

    Given a list of flux values (integers always >= 0), your task is to determine the unique energy signature 
    by using the following steps:
    - Find the element with maximum occurrence. If there are multiple, select the smallest one.
    - Find the sum of all elements in the array.
    - Multiply the sum of all elements with the most occurred number.

    Return the result.

    >>> teleporter_energy_signature([1, 2, 3, 2, 1, 2, 5, 1, 6])
    23

    Explanation: The number 2 and 1 appear thrice in the list, but 1 is smaller. 
    The sum of all elements in the array is 23. So, 23 * 1 = 23
    """
    from collections import Counter
    counter = Counter(flux_values)
    max_occurrence = max(counter.values())
    max_occurrence_numbers = [num for (num, count) in counter.items() if count == max_occurrence]
    smallest_max_occurrence_number = min(max_occurrence_numbers)
    sum_of_elements = sum(flux_values)
    result = sum_of_elements * smallest_max_occurrence_number
    return result