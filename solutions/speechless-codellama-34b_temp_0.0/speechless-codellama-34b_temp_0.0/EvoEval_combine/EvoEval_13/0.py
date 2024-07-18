def filter_exchange(arr, lst1):
    arr = [num for num in arr if sum((int(digit) for digit in str(abs(num)))) > 0]
    even_lst1 = [num for num in lst1 if num % 2 == 0]
    odd_lst1 = [num for num in lst1 if num % 2 != 0]
    even_arr = [num for num in arr if num % 2 == 0]
    odd_arr = [num for num in arr if num % 2 != 0]
    if len(odd_lst1) > len(even_arr):
        return 'NO'
    return 'YES'