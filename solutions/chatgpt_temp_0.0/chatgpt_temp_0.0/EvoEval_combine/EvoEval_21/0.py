
from typing import List

def base_change_prefixes(x: int, base: int) -> List[str]:
    """ For a given number x and a base less than 10, first change the numerical base of x to the given base.
    Then return a list of all prefixes from the shortest to the longest of the new base representation of x.
    
    >>> base_change_prefixes(8, 3)
    ['2', '22']
    >>> base_change_prefixes(8, 2)
    ['1', '10', '100', '1000']
    >>> base_change_prefixes(7, 2)
    ['1', '11', '111']
    """
    result = []
    while x > 0:
        result.append(str(x % base))
        x //= base
    result.reverse()
    prefixes = []
    for i in range(len(result)):
        prefixes.append(''.join(result[:i + 1]))
    return prefixes