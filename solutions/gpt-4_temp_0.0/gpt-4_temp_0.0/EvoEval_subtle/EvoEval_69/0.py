
def search(lst):
    """
    You are given a non-empty list of positive integers. Return the smallest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
        search([4, 1, 2, 2, 3, 1]) == 1
        search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 1
        search([5, 5, 4, 4, 4]) == -1
    """
    freq_dict = {}
    for num in lst:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    sorted_dict = dict(sorted(freq_dict.items()))
    for (key, value) in sorted_dict.items():
        if value >= key:
            return key
    return -1