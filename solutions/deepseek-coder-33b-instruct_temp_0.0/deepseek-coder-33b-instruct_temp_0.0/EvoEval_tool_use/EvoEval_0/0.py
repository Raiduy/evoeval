def get_digit_count(n: int) -> int:
    return len(str(n))
from typing import List, Tuple

def distribute_candies(candies: List[int], n: int) -> List[int]:
    """ Distribute the candies to a number of children in clockwise order. Each child should receive 
    candies equivalent to the number of digits in their position number. For example, the 10th child 
    should receive candies equal to the number of digits in 10, i.e., 2.
    
    The distribution continues until all candies are distributed. If there are not enough candies 
    for all children in a round of distribution, distribute the remaining candies to the children 
    starting from the first until the candies run out.
    
    The function should return a list showing the number of candies each child received in the order 
    they received them.

    >>> distribute_candies([100, 200, 300, 400, 500], 3)
    [500, 500, 500]
    >>> distribute_candies([45, 59, 78, 92, 100], 4)
    [94, 94, 93, 93]
    """
    child_candies = [0] * n
    candy_index = 0
    while candies:
        for i in range(n):
            if candy_index < len(candies):
                child_candies[i] += min(get_digit_count(candies[candy_index]), candies[candy_index])
                candies[candy_index] -= min(get_digit_count(candies[candy_index]), candies[candy_index])
                if candies[candy_index] == 0:
                    candy_index += 1
            else:
                break
    return child_candies