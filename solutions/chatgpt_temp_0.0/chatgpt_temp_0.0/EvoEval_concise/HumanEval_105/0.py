
def by_length(arr):
    """
    This function takes an array of integers and performs a series of operations. It first filters out numbers 
    that are not between 1 and 9 inclusive. Then, it sorts the resulting array in ascending order, reverses it, 
    and replaces each digit with its corresponding English word 
    ("One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine").

    Example:
      For input array [2, 1, 1, 4, 5, 8, 2, 3], the function returns ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"].
      For an empty array, it returns an empty array.
      For an array with integers outside the 1-9 range, such as [1, -1 , 55], the function ignores those numbers and returns ['One'].
    """
    filtered_arr = [num for num in arr if 1 <= num <= 9]
    sorted_arr = sorted(filtered_arr)
    reversed_arr = sorted_arr[::-1]
    word_arr = []
    for num in reversed_arr:
        if num == 1:
            word_arr.append('One')
        elif num == 2:
            word_arr.append('Two')
        elif num == 3:
            word_arr.append('Three')
        elif num == 4:
            word_arr.append('Four')
        elif num == 5:
            word_arr.append('Five')
        elif num == 6:
            word_arr.append('Six')
        elif num == 7:
            word_arr.append('Seven')
        elif num == 8:
            word_arr.append('Eight')
        elif num == 9:
            word_arr.append('Nine')
    return word_arr