
def add(lst):
    """Sum the even numbers at odd indices in a non-empty list of integers, lst.

    Examples:
        add([4, 2, 6, 7]) ==> 2 
    """
    sum_even_odd_index = 0
    for (index, number) in enumerate(lst):
        if index % 2 != 0 and number % 2 == 0:
            sum_even_odd_index += number
    return sum_even_odd_index