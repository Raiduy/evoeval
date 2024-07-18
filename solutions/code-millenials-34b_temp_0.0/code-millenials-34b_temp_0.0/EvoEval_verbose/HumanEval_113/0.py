
def odd_count(lst):
    output = []
    for (i, s) in enumerate(lst):
        count = sum((1 for c in s if int(c) % 2 != 0))
        result_string = 'the number of odd elements {0}n the str{0}ng {0} of the {0}nput.'.format(count)
        output.append(result_string)
    return output