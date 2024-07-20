def check_data(data):
    """
    Check if the input data is a list and if all elements of the list are integers.

    :param data: list of elements
    :return: boolean - True if the input is a list of integers, False otherwise.
    """

    if not isinstance(data, list):
        return False

    for element in data:
        if not isinstance(element, int):
            return False

    return True

def custom_list_parser(lst):
    """
    Given a list of integers, return a new list where elements are replaced as per the following rules:
    - If an element is positive, replace the element with its square.
    - If an element is negative, replace the element with its absolute value.

    If the input is not a valid list of integers, the function should return None.

    Examples:
    custom_list_parser([1, 2, -3, 4]) == [1, 4, 3, 16]
    custom_list_parser([-5, -4, -3, 2]) == [5, 4, 3, 4]
    custom_list_parser([]) == []
    """
    if not check_data(lst):
        return None
    return [x ** 2 if x > 0 else abs(x) for x in lst]