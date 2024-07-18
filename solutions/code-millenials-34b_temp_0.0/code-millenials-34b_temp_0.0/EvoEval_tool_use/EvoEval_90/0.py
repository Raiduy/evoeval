def is_valid_input(lst):
    '''
    This helper function checks if the input is a list of integers.
    
    Parameters: 
    lst (list): list of integers

    Returns:
    boolean: True if the input is a list of integers, False otherwise 

    Examples: 
    is_valid_input([1, 2, 3]) ➞ True
    is_valid_input([1, '2', 3]) ➞ False
    is_valid_input([1, 2.0, 3]) ➞ False
    is_valid_input([]) ➞ False
    '''
    if not lst or type(lst) != list:
        return False
    return all(isinstance(i, int) for i in lst)
def find_max_product_sublist(lst):
    if not is_valid_input(lst):
        return 'Invalid input'
    if not lst:
        return None
    max_product = current_product = lst[0]
    for i in range(1, len(lst)):
        if lst[i] < 0:
            current_product = 1
        else:
            current_product *= lst[i]
        max_product = max(max_product, current_product)
    return max_product