
def odd_count(lst):
    result = []
    for string in lst:
        count = sum(1 for char in string if int(char) % 2 != 0)
        result.append(f"the number of odd elements {count}n the str{count}ng {count} of the {count}nput.")
    return result
