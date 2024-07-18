
def get_max_even_positive(l: list):
    """This function takes a list of positive and negative numbers, filters 
    out the negative numbers, and returns the largest even number among the 
    remaining elements. If there are no positive even numbers in the list, 
    the function should return -1.

    For example:
    get_max_even_positive([-1, 2, -4, 5, 6]) = 6
    get_max_even_positive([1, 3, 5, 7]) = -1
    """
    positive_even_numbers = [num for num in l if num > 0 and num % 2 == 0]
    if not positive_even_numbers:
        return -1
    return max(positive_even_numbers)