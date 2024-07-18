
def odd_count(lst):
    output = []
    for string in lst:
        odd_count = sum((1 for digit in string if int(digit) % 2 != 0))
        output.append(f'the number of odd elements {odd_count}n the str{odd_count}ng {odd_count} of the {odd_count}nput.')
    return output