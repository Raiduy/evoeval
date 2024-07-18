def strange_sort_list(lst, lst2):
    merged = lst + lst2
    merged = list(set(merged))
    odd_numbers = [num for num in merged if num % 2 != 0 and num in lst]
    even_numbers = [num for num in merged if num % 2 == 0 and num in lst]
    other_numbers = sorted([num for num in merged if num not in lst], reverse=True)
    result = []
    while odd_numbers or even_numbers or other_numbers:
        if odd_numbers:
            result.append(odd_numbers.pop())
        if even_numbers:
            result.append(even_numbers.pop())
        if other_numbers:
            result.append(other_numbers.pop())
    return result