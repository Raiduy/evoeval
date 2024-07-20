
def odd_count(lst):
    output = []
    for s in lst:
        odd_count = sum((1 for c in s if int(c) % 2 != 0))
        output.append('the number of odd elements {}n the str{}ng {} of the {}nput.'.format(odd_count, odd_count, odd_count, odd_count))
    return output