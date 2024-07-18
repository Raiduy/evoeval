


def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    # Initialize the sum
    total_sum = 0
    
    # Iterate through the list with index
    for i, num in enumerate(lst):
        # Check if the index is a multiple of 3
        if i % 3 == 0:
            total_sum += num ** 2
        # Check if the index is a multiple of 4 but not a multiple of 3
        elif i % 4 == 0:
            total_sum += num ** 3
        # If the index is not a multiple of 3 or 4, add the number as it is
        else:
            total_sum += num
    
    return total_sum
