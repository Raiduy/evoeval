def specialFilter(nums):
    count = 0
    odd_digits = {'1', '3', '5', '7', '9'}
    for num in nums:
        if num > 10:
            num_str = str(num)
            if num_str[0] in odd_digits and num_str[-1] in odd_digits:
                count += 1
    return count