
def sort_count_nums(arr):
    """
    Function to sort an array based on the count of numbers with sum of digits > 0.
    """
    count_positive_sum = sum((1 for num in arr if sum_of_digits(num) > 0))
    if count_positive_sum % 2 == 1:
        return sorted(arr)
    else:
        return sorted(arr, reverse=True)