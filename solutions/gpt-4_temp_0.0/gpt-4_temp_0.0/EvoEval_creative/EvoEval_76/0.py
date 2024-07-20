def create_pyramid(lst):
    """
    You are given a list of positive integers. 
    Your task is to create a pyramid out of the numbers, where every level of the pyramid 
    is represented by a string of equal length. The number of characters in a string equals 
    the sum of the positive integers in the corresponding level of the pyramid.
    The pyramid should be built from the bottom up, i.e. the first element of the list 
    should form the bottom level of the pyramid.
    Return the pyramid as a list of strings. If the list of integers is empty, return an 
    empty list.

    Note: Use the character '#' to represent the numbers.

    Examples:
    create_pyramid([3, 2, 1]) == ['#', '##', '###']
    create_pyramid([5, 4, 2]) == ['##', '####', '#####']
    create_pyramid([]) == []
    """
    pyramid = []
    for num in lst:
        pyramid.insert(0, '#' * num)
    return pyramid