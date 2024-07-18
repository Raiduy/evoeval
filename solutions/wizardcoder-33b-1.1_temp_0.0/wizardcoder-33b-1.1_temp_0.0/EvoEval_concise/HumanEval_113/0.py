
def odd_count(lst):
    result = []
    for (i, s) in enumerate(lst, 1):
        count = sum((int(c) % 2 for c in s))
        result.append(f'the number of odd elements {count}n the str{count}ng {count} of the {count}nput.')
    return result