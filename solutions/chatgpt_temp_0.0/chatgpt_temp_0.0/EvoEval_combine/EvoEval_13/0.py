def filter_exchange(arr, lst1):

    def sum_of_digits(num):
        return sum((int(digit) for digit in str(abs(num))))
    filtered_arr = [num for num in arr if sum_of_digits(num) > 0]
    if not filtered_arr:
        return 'NO'
    even_count = sum((1 for num in lst1 if num % 2 == 0))
    odd_count = len(lst1) - even_count
    if odd_count > len(filtered_arr):
        return 'NO'
    else:
        return 'YES'