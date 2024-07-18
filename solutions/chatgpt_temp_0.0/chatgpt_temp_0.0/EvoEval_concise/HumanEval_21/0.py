from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """
    Transforms a list of numbers by rescaling values between 0 and 1 
    where smallest becomes 0 and largest becomes 1.

    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    min_val = min(numbers)
    max_val = max(numbers)
    rescaled_numbers = [(x - min_val) / (max_val - min_val) for x in numbers]
    return rescaled_numbers