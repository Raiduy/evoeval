def sort_third_modified(l: list, m: list) -> list:
    concatenated_list = l + m
    divisible_by_three = [concatenated_list[i] for i in range(len(concatenated_list)) if (i + 1) % 3 == 0]
    divisible_by_three_sorted = sorted(divisible_by_three, reverse=True)
    result_list = []
    divisible_index = 0
    for i in range(len(concatenated_list)):
        if (i + 1) % 3 == 0:
            result_list.append(divisible_by_three_sorted[divisible_index])
            divisible_index += 1
        else:
            result_list.append(concatenated_list[i])
    return result_list