
def odd_count(lst):
    """Given a list of digit-only strings, this function returns a new list. Each element i of the new list is a string describing the count of odd digits in the i'th input string.

    >>> odd_count(['1234567'])
    ["the number of odd elements in the string 1234567 of the input."]
    >>> odd_count(['3',"11111111"])
    ["the number of odd elements in the string 3 of the input.",
     "the number of odd elements in the string 11111111 of the input."]
    """
    result = []
    for string in lst:
        count = 0
        for digit in string:
            if int(digit) % 2 != 0:
                count += 1
        result.append('the number of odd elements in the string {} of the input.'.format(string))
    return result