
def odd_count(lst):
    result = []
    for (i, s) in enumerate(lst):
        count = sum((int(c) % 2 for c in s))
        result.append(f'the number of odd elements {count}n the str{count}ng {i + 1} of the {i + 1}nput.')
    return result