def odd_count_base_change(lst, base):
    result = []
    for (i, s) in enumerate(lst):
        odd_count = sum((1 for c in s if int(c, base) % 2 == 1))
        result.append(f'the number of odd elements {odd_count}n the str{odd_count}ng {odd_count} of the {odd_count}nput.')
    return result