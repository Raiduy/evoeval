def sum_squares(lst):
    """
    This function is designed to perform certain mathematical operations on a list of integers, 'lst', based on the index position of each 
    integer in the list. The operations and their conditions are as follows: 

    1. If an integer's index is a multiple of 3, the function will square that integer.
    2. If an integer's index is a multiple of 4, but not a multiple of 3, the function will cube that integer.
    3. If an integer's index is not a multiple of either 3 or 4, the function will leave that integer unchanged. 

    After performing the above operations, the function will then sum together all the entries in the list and return this sum. 

    It's important to note that Python uses zero-based indexing, so the first element of the list is at index 0, the second element is at 
    index 1, and so on. 

    If an empty list is provided, the function will simply return 0, as there are no entries to perform operations on and sum together.

    Examples:
    Let's see how the function works in detail with a few examples: 

    For lst = [1,2,3], the output should be 6. Here's how:
      - The integer at index 0 (1) is squared, because 0 is a multiple of 3, resulting in 1.
      - The integer at index 1 (2) is left unchanged, because 1 is neither a multiple of 3 nor 4, resulting in 2.
      - The integer at index 2 (3) is left unchanged, because 2 is neither a multiple of 3 nor 4, resulting in 3.
      - The sum of these entries is 1 + 2 + 3 = 6.

    For lst = [], the output should be 0, as there are no entries to perform operations on.

    For lst = [-1,-5,2,-1,-5], the output should be -126. Here's how:
      - The integer at index 0 (-1) is squared, because 0 is a multiple of 3, resulting in 1.
      - The integer at index 1 (-5) is left unchanged, because 1 is neither a multiple of 3 nor 4,
      - The integer at index 2 (2) is left unchanged, because 2 is neither a multiple of 3 nor 4, 
      - The integer at index 3 (-1) is squared, resulting in 1,
      - The integera at index 4 (-5) is cubed, resulting in -125,
      - The sum of these entries is -126 
    """
    result = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            result += lst[i] ** 2
        elif i % 4 == 0:
            result += lst[i] ** 3
        else:
            result += lst[i]
    return result