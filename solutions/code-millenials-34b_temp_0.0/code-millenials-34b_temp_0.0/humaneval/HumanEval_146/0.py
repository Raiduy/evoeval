
def specialFilter(nums):
    count = 0
    for num in nums:
        if num > 10:
            str_num = str(abs(num))
            if len(str_num) > 1 and str_num[0] in '13579' and str_num[-1] in '13579':
                count += 1
    return count
