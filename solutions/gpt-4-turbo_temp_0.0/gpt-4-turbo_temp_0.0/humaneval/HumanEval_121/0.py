
def solution(lst):
    """Given a non-empty list of integers, return the sum of all of the odd elements that are in even positions."""
    # Initialize sum of odd elements in even positions
    sum_odd_even_pos = 0
    
    # Iterate through the list with index
    for index, value in enumerate(lst):
        # Check if the index is even and the value is odd
        if index % 2 == 0 and value % 2 != 0:
            sum_odd_even_pos += value
            
    return sum_odd_even_pos
