
def specialFilter(nums):
    def is_odd_digit(n):
        str_n = str(n)
        return int(str_n[0]) % 2 == 1 and int(str_n[-1]) % 2 == 1

    count = 0
    for num in nums:
        if num > 10 and is_odd_digit(num):
            count += 1
    return count
