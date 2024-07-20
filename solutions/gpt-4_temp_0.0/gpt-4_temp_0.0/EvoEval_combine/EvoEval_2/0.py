
from typing import List

def modp_intersperse(numbers: List[int], n: int, p: int) -> List[int]:
    """ Insert the result of 2^n modulo p between every two consecutive elements of input list `numbers'
    >>> modp_intersperse([], 3, 5)
    []
    >>> modp_intersperse([1, 2, 3], 3, 5)
    [1, 3, 2, 3, 3]
    >>> modp_intersperse([10, 20, 30], 1101, 101)
    [10, 2, 20, 2, 30]
    """
    result = []
    mod_value = pow(2, n) % p
    for num in numbers:
        result.append(num)
        result.append(mod_value)
    return result[:-1]