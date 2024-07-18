
def specialFilter(nums):
    """
    Returns the count of numbers from the given list that are greater than 10 and have both first and last digits odd.
    
    Example:
    specialFilter([15, -73, 14, -15]) => 1
    specialFilter([33, -2, -3, 45, 21, 109]) => 2
    """
    count = 0
    for num in nums:
        if num > 10:
            str_num = str(num)
            first_digit = int(str_num[0])
            last_digit = int(str_num[-1])
            if first_digit % 2 != 0 and last_digit % 2 != 0:
                count += 1
    return count