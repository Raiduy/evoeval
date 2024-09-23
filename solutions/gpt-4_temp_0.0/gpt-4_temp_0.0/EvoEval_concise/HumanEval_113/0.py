
def odd_count(lst):
    """Given a list of digit-only strings, this function returns a new list. Each element i of the new list is a string describing the count of odd digits in the i'th input string.

    >>> odd_count(['1234567'])
    ["the number of odd elements 4 in the string 1 of the input."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements 1 in the string 1 of the input.",
     "the number of odd elements 8 in the string 2 of the input."]
    """
    result = []
    for (i, s) in enumerate(lst, start=1):
        odd_count = sum((1 for c in s if int(c) % 2 != 0))
        result.append(f'the number of odd elements {odd_count} in the string {i} of the input.')
    return result