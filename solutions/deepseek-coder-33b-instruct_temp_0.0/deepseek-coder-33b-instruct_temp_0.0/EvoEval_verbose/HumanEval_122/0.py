
def add_elements(arr, k):
    """
    This function takes in two parameters, a non-empty array of integers 'arr' and an integer 'k'.
    The function's primary goal is to return the sum of the elements that have at most two digits from the first 'k' elements of 'arr'.

    Parameter:
    arr: A non-empty list of integers. The size of the list can range from 1 to 100.
    k: An integer representing the number of first elements from the array 'arr' to consider for the operation. The value of 'k' is always greater than or equal to 1 and less than or equal to the length of the array 'arr'.

    The function iterates over the first 'k' elements of the array 'arr'. For each element in this iteration, it checks whether the element has at most two digits. If an element has more than two digits, it is ignored. Otherwise, it is added to a running total. Finally, the function returns the total sum.

    Example:

        Given the array 'arr' as [111,21,3,4000,5,6,7,8,9] and 'k' as 4, the function will iterate over the first 4 elements of the array, i.e., 111, 21, 3, and 4000.
        Out of these, 111 and 4000 have more than two digits and therefore, are ignored.
        The elements 21 and 3 have two and one digits, respectively. Therefore, they are included in the sum.
        The function finally returns the sum of these two elements, i.e., 24.

    Returns:
    int: The sum of the elements with at most two digits from the first 'k' elements of the array 'arr'.

    Constraints:
        1. The length of the array 'arr' is always greater than or equal to 1 and less than or equal to 100.
        2. The value of 'k' is always greater than or equal to 1 and less than or equal to the length of the array 'arr'.
    """
    total = 0
    for i in range(k):
        if len(str(arr[i])) <= 2:
            total += arr[i]
    return total