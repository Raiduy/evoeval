def filter_exchange(arr, lst1):
    filtered_arr = [num for num in arr if sum_of_digits(num) > 0]
    even_count_lst1 = sum((num % 2 == 0 for num in lst1))
    odd_count_lst1 = len(lst1) - even_count_lst1
    even_count_filtered_arr = sum((num % 2 == 0 for num in filtered_arr))
    odd_count_filtered_arr = len(filtered_arr) - even_count_filtered_arr
    if odd_count_lst1 <= even_count_filtered_arr:
        return 'YES'
    else:
        return 'NO'