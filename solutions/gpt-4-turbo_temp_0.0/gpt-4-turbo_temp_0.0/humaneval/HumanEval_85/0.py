
def add(lst):
    """Given a non-empty list of integers lst, add the even elements that are at odd indices.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    # Initialize sum of even elements at odd indices
    sum_even_odd_idx = 0
    
    # Iterate through the list with index
    for idx, num in enumerate(lst):
        # Check if the index is odd and the number is even
        if idx % 2 != 0 and num % 2 == 0:
            sum_even_odd_idx += num
    
    return sum_even_odd_idx
