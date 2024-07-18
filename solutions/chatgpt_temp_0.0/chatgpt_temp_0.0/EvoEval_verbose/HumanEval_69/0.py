
def search(lst):
    """
    This function is designed to handle a particular problem involving number patterns in a list. 
    The function takes one argument, a non-empty list of positive integers, and uses this list to 
    return a specific response based on the frequency of integers in the list.

    More specifically, this function will search through the provided list and identify the greatest 
    integer that not only exceeds zero but also appears in the list a number of times greater than 
    or equal to its actual value. For example, if the integer 2 appears at least 2 times in the list, 
    it could be a potential candidate for the return value. Similarly, if the integer 3 appears 3 or 
    more times in the list, it could also be a candidate for the return value. The function will 
    return the greatest integer that meets this criteria. 

    The frequency of a particular integer is determined by counting the number of times it appears 
    in the list. For example, if the integer 2 appears 3 times in the list, its frequency is 3.

    If there are no integers in the list that meet this criteria, the function will return -1.

    Examples:
        If the function is given the list [4, 1, 2, 2, 3, 1], it will return the integer 2. This is 
        because 2 is the greatest integer in the list that appears a frequency greater than or equal 
        to its own value.

        If the function is given the list [1, 2, 2, 3, 3, 3, 4, 4, 4], it will return the integer 3. 
        This is because 3 is the greatest integer in the list that appears a frequency greater than 
        or equal to its own value.

        If the function is given the list [5, 5, 4, 4, 4], it will return -1. In this case, none 
        of the integers in the list appear a frequency greater than or equal to its own value.
    """
    max_candidate = -1
    for num in lst:
        if num > 0 and lst.count(num) >= num:
            if num > max_candidate:
                max_candidate = num
    return max_candidate