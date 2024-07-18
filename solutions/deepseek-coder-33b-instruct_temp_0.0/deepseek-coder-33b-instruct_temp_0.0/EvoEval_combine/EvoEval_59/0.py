def odd_count_base_change(lst, base):

    def base_change(num, base):
        if num == 0:
            return '0'
        nums = []
        while num:
            (num, rem) = divmod(num, base)
            nums.append(str(rem))
        return ''.join(reversed(nums))

    def count_odd(num):
        return sum((1 for digit in num if int(digit) % 2 != 0))
    result = []
    for (i, num) in enumerate(lst, 1):
        base_num = base_change(int(num), base)
        odd_count = count_odd(base_num)
        result.append(f'the number of odd elements {odd_count}n the str{odd_count}ng {odd_count} of the {odd_count}nput.')
    return result