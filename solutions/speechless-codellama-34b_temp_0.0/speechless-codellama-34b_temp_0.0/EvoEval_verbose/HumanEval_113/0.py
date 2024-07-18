
def odd_count(lst):
    result = []
    for (i, string) in enumerate(lst):
        odd_digits = sum((int(digit) % 2 for digit in string))
        result.append(f'the number of odd elements {odd_digits}n the str{odd_digits}ng {odd_digits} of the {odd_digits}nput.')
    return result