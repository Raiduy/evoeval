def strange_sort_list(lst, lst2):
    merged_list = lst + lst2
    merged_list = list(set(merged_list))
    odd_nums = [num for num in merged_list if num % 2 != 0]
    even_nums = [num for num in merged_list if num % 2 == 0]
    odd_nums.sort()
    even_nums.sort(reverse=True)
    result = []
    while odd_nums and even_nums:
        result.append(odd_nums.pop(0))
        result.append(even_nums.pop(0))
    result.extend(odd_nums)
    result.extend(even_nums)
    return result