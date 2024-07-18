def specialFilter(nums):
    """
    This function is named 'specialFilter' and it accepts a single input argument 'nums', which is expected to be a list of integers.

    The purpose of this function is to calculate and return a count of the number of elements in the 'nums' list that fulfill both of the following criteria:
    1. The numeric value of the element is greater than 10.
    2. Both the first and last digits of the element are odd numbers. The set of odd numbers is defined as {1, 3, 5, 7, 9}.

    Let's consider some examples for a better understanding:

    EXAMPLES:

    If the function is called with the list [15, -73, 14, -15] like so: specialFilter([15, -73, 14, -15]), 
    it will return 1 as there is just one number (15) that is greater than 10 and has both first and last digits as odd numbers.

    If the function is called with the list [33, -2, -3, 45, 21, 109] like so: specialFilter([33, -2, -3, 45, 21, 109]), 
    it will return 2 as there are two numbers (33, 109) that are greater than 10 and have both first and last digits as odd numbers.

    So, in general, the function specialFilter(nums) will process the 'nums' list and return a count of elements that satisfy the above-mentioned criteria. 
    """
    count = 0
    odd_digits = {'1', '3', '5', '7', '9'}
    for num in nums:
        if num > 10:
            str_num = str(num)
            if str_num[0] in odd_digits and str_num[-1] in odd_digits:
                count += 1
    return count