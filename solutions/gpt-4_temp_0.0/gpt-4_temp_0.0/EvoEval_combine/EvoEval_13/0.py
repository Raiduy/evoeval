def filter_exchange(arr, lst1):
    arr = [num for num in arr if sum((int(digit) for digit in str(abs(num)))) > 0]
    odd_nums_in_lst1 = [num for num in lst1 if num % 2 != 0]
    even_nums_in_arr = [num for num in arr if num % 2 == 0]
    if len(odd_nums_in_lst1) <= len(even_nums_in_arr):
        return 'YES'
    else:
        return 'NO'