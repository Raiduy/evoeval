
def odd_count(lst):
    result = []
    for string in lst:
        count = sum(int(digit) % 2 != 0 for digit in string)
        result.append("the number of odd elements in the string {} of the input.".format(count))
    return result
