def odd_count_base_change(lst, base):
    res = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit, base) % 2 != 0:
                count += 1
        s = f'the number of odd elements {count}n the str{count}ng {count} of the {count}nput.'
        res.append(s)
    return res