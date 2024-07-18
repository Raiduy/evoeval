
def add(lst):
    """Sum the even numbers at odd indices in a non-empty list of integers, lst.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    sum = 0
    for i in range(len(lst)):
        if i % 2 != 0 and lst[i] % 2 == 0:
            sum += lst[i]
    return sum