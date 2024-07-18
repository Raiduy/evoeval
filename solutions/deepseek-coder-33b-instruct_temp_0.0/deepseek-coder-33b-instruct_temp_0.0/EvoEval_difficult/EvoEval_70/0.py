def strange_sort_list(lst, lst2):
    merged_list = lst + lst2
    merged_list = list(set(merged_list))
    odd_numbers = [num for num in merged_list if num % 2 != 0]
    even_numbers = [num for num in merged_list if num % 2 == 0]
    odd_numbers.sort()
    even_numbers.sort()
    result = []
    while odd_numbers or even_numbers:
        if odd_numbers:
            result.append(odd_numbers.pop(0))
        if even_numbers:
            result.append(even_numbers.pop(0))
    return result