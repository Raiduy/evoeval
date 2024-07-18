
def sum_square_cube_to_n(n: int) -> int:
    """
    This function takes an integer n. The function generates a list of integers from 1 to n inclusive. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries.

    Examples:
    For n = 3 the output should be 12
    For n = 1 the output should be 1
    For n = 5 the output should be 81
    For n = 10 the output should be 727
    """
    total_sum = 0
    for i in range(1, n + 1):
        if i % 3 == 0:
            total_sum += i ** 2
        elif i % 4 == 0:
            total_sum += i ** 3
        else:
            total_sum += i
    return total_sum