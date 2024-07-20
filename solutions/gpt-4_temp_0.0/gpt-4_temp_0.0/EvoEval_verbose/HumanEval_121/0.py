
def solution(lst):
    """
    This function takes as input a non-empty list of integers. Its purpose is to compute and return the sum of all odd elements 
    located at even positions within this list. 

    The position of elements is 0-indexed, meaning the first element is considered to be at position 0, the second element at 
    position 1, and so on. When we refer to "odd elements", we mean the actual integer value of the element is odd (not divisible by 2). 
    Similarly, when we say "even positions", we mean the position/index of the element in the list is even. 

    The function does not modify the original list and does not have any side effects. If there are no odd elements in even positions,
    the function returns 0. The function does not handle empty lists and assumes that the input list is always non-empty.

    Examples:
    Given the list [5, 8, 7, 1], the function would return 12, because 5 and 7 are odd numbers and they are at positions 0 and 2, 
    which are even.

    Given the list [3, 3, 3, 3, 3], the function would return 9, because the numbers at positions 0, 2, and 4 are all 3, which is 
    odd, and their sum is 9.

    Given the list [30, 13, 24, 321], the function would return 0, because there are no odd numbers at even positions.
    """
    return sum((lst[i] for i in range(0, len(lst), 2) if lst[i] % 2 != 0))