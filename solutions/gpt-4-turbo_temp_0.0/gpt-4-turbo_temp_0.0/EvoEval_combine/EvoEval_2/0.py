
from typing import List

def modp_intersperse(numbers: List[int], n: int, p: int) -> List[int]:
    """ Insert the result of 2^n modulo p between every two consecutive elements of input list `numbers' """
    if not numbers:
        return []
    mod_result = pow(2, n, p)
    interspersed_list = []
    for number in numbers[:-1]:
        interspersed_list.append(number)
        interspersed_list.append(mod_result)
    interspersed_list.append(numbers[-1])
    return interspersed_list