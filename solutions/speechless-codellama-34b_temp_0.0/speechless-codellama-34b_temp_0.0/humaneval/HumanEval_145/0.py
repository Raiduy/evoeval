
def order_by_points(nums):
    """
    Sorts the given list of integers in ascending order according to the sum of their digits.
    """
    # Create a list of tuples, where each tuple contains an integer and its sum of digits
    nums_with_points = [(num, sum(int(digit) for digit in str(abs(num)))) for num in nums]
    
    # Sort the list of tuples based on the sum of digits, and then by index in the original list
    sorted_nums = sorted(nums_with_points, key=lambda x: (x[1], nums.index(x[0])))
    
    # Extract the sorted integers from the list of tuples
    sorted_nums = [num for num, points in sorted_nums]
    
    return sorted_nums
