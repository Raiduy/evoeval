
def double_the_difference(lst):
    '''
    Given a list of numbers, return the sum of squares of the numbers
    in the list that are odd. Ignore numbers that are negative or not integers.
    
    double_the_difference([1, 3, 2, 0]) == 1 + 9 + 0 + 0 = 10
    double_the_difference([-1, -2, 0]) == 0
    double_the_difference([9, -2]) == 81
    double_the_difference([0]) == 0  
    
    If the input list is empty, return 0.
    '''
    # Initialize the sum
    sum_of_squares = 0
    
    # Iterate through each number in the list
    for num in lst:
        # Check if the number is odd, positive, and an integer
        if isinstance(num, int) and num > 0 and num % 2 != 0:
            # Add the square of the number to the sum
            sum_of_squares += num ** 2
    
    # Return the final sum
    return sum_of_squares