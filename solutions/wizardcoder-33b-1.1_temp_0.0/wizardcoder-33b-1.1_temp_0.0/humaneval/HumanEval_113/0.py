
def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        odd_count = sum(int(c) % 2 for c in s)
        result.append(f"the number of odd elements {odd_count}n the str{odd_count}ng {odd_count} of the {odd_count}nput.")
    return result
