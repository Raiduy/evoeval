
def add(lst):
    """Given a non-empty list of integers lst, add the odd elements that are at even indices.


    Examples:
        add([4, 2, 5, 7]) ==> 5
    """
    sum = 0
    for i in range(len(lst)):
        if i % 2 == 0 and lst[i] % 2 != 0:
            sum += lst[i]
    return sum