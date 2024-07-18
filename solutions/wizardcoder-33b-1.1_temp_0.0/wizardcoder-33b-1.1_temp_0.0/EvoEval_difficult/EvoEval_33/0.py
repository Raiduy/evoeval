def sort_third_modified(l: list, m: list):
    concat_list = l + m
    divisible_by_3 = [concat_list[i] for i in range(len(concat_list)) if i % 3 == 0]
    divisible_by_3.sort(reverse=True)
    for i in range(len(concat_list)):
        if i % 3 == 0:
            concat_list[i] = divisible_by_3.pop(0)
    return concat_list