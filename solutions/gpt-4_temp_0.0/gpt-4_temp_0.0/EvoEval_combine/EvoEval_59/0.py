def odd_count_base_change(lst, base):
    """Given a list of strings and a base number, 
    where each string consists of only digits, 
    return a list where each element k of the output should be 
    "the number of odd elements in the string i of the input." 
    where all the i's are replaced by the number of odd digits in the k'th string 
    of the input after changing the base of each digit to the given base.

    >>> odd_count_base_change(['1234567'], 2)
    ["the number of odd elements 12n the str12ng 12 of the 12nput."]
    >>> odd_count_base_change(['3',"11111111"], 3)
    ["the number of odd elements 1n the str1ng 1 of the 1nput.",
     "the number of odd elements 8n the str8ng 8 of the 8nput."]
    """
    result = []
    for s in lst:
        odd_count = sum((1 for c in s if int(c, base) % 2 == 1))
        result.append('the number of odd elements {}n the str{}ng {} of the {}nput.'.format(odd_count, odd_count, odd_count, odd_count))
    return result