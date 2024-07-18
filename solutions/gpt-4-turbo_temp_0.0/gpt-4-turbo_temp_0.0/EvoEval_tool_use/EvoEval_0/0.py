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
    """
    children_candies = [0] * n
    position = 1
    for candy in candies:
        while candy > 0:
            digit_count = get_digit_count(position)
            if candy >= digit_count:
                children_candies[(position - 1) % n] += digit_count
                candy -= digit_count
            else:
                children_candies[(position - 1) % n] += candy
                candy = 0
            position += 1
    return children_candies