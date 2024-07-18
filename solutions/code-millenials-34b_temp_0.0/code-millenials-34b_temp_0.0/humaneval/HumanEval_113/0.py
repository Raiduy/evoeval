
def odd_count(lst):
    result = []
    for i, s in enumerate(lst):
        count = sum(1 for c in s if int(c) % 2 != 0)
        string = "the number of odd elements {}n the str{}ng {} of the {}nput.".format(count, count, count, count)
        result.append(string)
    return result
