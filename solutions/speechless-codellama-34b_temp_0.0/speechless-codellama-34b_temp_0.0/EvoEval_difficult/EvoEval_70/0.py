def strange_sort_list(lst, lst2):
    merged_list = lst + lst2
    merged_list = list(set(merged_list))
    odd_numbers = [num for num in merged_list if num % 2 != 0]
    even_numbers = [num for num in merged_list if num % 2 == 0]
    sorted_odd_numbers = sorted(odd_numbers)
    sorted_even_numbers = sorted(even_numbers, reverse=True)
    combined_numbers = sorted_odd_numbers + sorted_even_numbers
    remaining_numbers = [num for num in merged_list if num not in odd_numbers and num not in even_numbers]
    sorted_remaining_numbers = []
    while remaining_numbers:
        sorted_remaining_numbers.append(min(remaining_numbers))
        remaining_numbers.remove(min(remaining_numbers))
        if remaining_numbers:
            sorted_remaining_numbers.append(max(remaining_numbers))
            remaining_numbers.remove(max(remaining_numbers))
    sorted_list = combined_numbers + sorted_remaining_numbers
    return sorted_list