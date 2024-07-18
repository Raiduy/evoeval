def odd_count_base_change(lst, base):

    def count_odd_digits(num, base):
        count = 0
        while num > 0:
            digit = num % base
            if digit % 2 != 0:
                count += 1
            num //= base
        return count
    result = []
    for string in lst:
        odd_count = count_odd_digits(int(string), base)
        result.append('the number of odd elements {}n the str{}ng {} of the {}nput.'.format(odd_count, odd_count, odd_count, odd_count))
    return result