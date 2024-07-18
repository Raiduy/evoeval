
def odd_count(lst):
    output = []
    for string in lst:
        count = sum((int(digit) % 2 != 0 for digit in string))
        output.append('the number of odd elements in the string {} of the input.'.format(count))
    return output