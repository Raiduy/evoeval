def order_by_points(nums):
    digit_sums = {}
    for num in nums:
        digit_sum = sum((int(digit) for digit in str(abs(num))))
        if digit_sum not in digit_sums:
            digit_sums[digit_sum] = []
        digit_sums[digit_sum].append(num)
    sorted_keys = sorted(digit_sums.keys())
    sorted_nums = []
    for key in sorted_keys:
        sorted_nums.extend(digit_sums[key])
    return sorted_nums