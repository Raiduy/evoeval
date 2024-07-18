def specialFilter(nums):
    count = 0
    for num in nums:
        num_abs = abs(num)
        num_str = str(num_abs)
        if num > 10:
            if int(num_str[0]) % 2 != 0 and int(num_str[-1]) % 2 != 0:
                count += 1
    return count