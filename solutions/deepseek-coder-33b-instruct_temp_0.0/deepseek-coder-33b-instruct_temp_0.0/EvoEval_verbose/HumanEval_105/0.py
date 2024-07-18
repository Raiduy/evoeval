
def by_length(arr):
    """
    The purpose of this function 'by_length' is to manipulate a given array of integers, specifically those that fall within the range of 1 to 9 inclusive. 

    The function processes the input in the following way:
    1. The function first filters the array to only keep integers between 1 and 9. This is done to ignore any "strange" numbers which do not fall within this range. 
    2. It then sorts the resulting filtered array in ascending order. 
    3. After sorting, the array is reversed, resulting in a descending order of the integers. 
    4. Finally, each digit that corresponds to a number between 1 and 9 inclusive is replaced by its equivalent word form as spelled out in English - "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine". 

    Args:
    arr (list): A list of integers.

    Returns:
    list: A list of strings, with each string being the English word equivalent of each digit in the processed input array. If the input array is empty, an empty list is returned.

    Example:
    If the input is arr = [2, 1, 1, 4, 5, 8, 2, 3], the output will be ["Eight", "Five", "Four", "Three", "Two", "Two", "One", "One"]. This is because the function first sorts the array to get [1, 1, 2, 2, 3, 4, 5, 8] then reverses it to get [8, 5, 4, 3, 2, 2, 1, 1] and then replaces each digit with its English word equivalent.

    Another example, if the input is arr = [1, -1 , 55] which includes "strange" numbers, the output will be ['One']. This is because -1 and 55 are ignored as they are outside the range of 1 to 9 inclusive. The remaining number 1 is then replaced with its English word equivalent.
    """
    arr = [i for i in arr if 1 <= i <= 9]
    arr.sort()
    arr.reverse()
    arr = ['One' if i == 1 else 'Two' if i == 2 else 'Three' if i == 3 else 'Four' if i == 4 else 'Five' if i == 5 else 'Six' if i == 6 else 'Seven' if i == 7 else 'Eight' if i == 8 else 'Nine' for i in arr]
    return arr