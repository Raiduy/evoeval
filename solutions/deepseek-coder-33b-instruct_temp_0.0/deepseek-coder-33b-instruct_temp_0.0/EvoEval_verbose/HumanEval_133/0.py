

def sum_squares(lst):
    """
    The function 'sum_squares' takes a list of numbers as an argument. The numbers in the list could be 
    positive, negative or zero and could also be integer or float numbers.

    The purpose of this function is to first round each number in the list to its nearest upper integer 
    (also known as its Ceiling value), then square each of these rounded numbers, and finally, return the 
    sum of all these squared numbers. 

    This function does not modify the original list and returns a single integer number that represents 
    the sum of the squared Ceiling values of all the numbers in the input list.

    Examples:

    If the input list is lst = [1,2,3], the function rounds up all the numbers (which are already integers) and 
    squares them to get [1,4,9]. The function then sums these numbers and returns the result 14.

    If the input list is lst = [1,4,9], the function rounds up all the numbers (which are already integers) and 
    squares them to get [1,16,81]. The function then sums these numbers and returns the result 98.

    If the input list is lst = [1,3,5,7], the function rounds up all the numbers (which are already integers) and 
    squares them to get [1,9,25,49]. The function then sums these numbers and returns the result 84.

    If the input list is lst = [1.4,4.2,0], the function first rounds up all the numbers to get [2,5,0] and 
    squares them to get [4,25,0]. The function then sums these numbers and returns the result 29.

    If the input list is lst = [-2.4,1,1], the function first rounds up all the numbers to get [-2,1,1] and 
    squares them to get [4,1,1]. The function then sums these numbers and returns the result 6.
    
    """
    return sum((math.ceil(num) ** 2 for num in lst))