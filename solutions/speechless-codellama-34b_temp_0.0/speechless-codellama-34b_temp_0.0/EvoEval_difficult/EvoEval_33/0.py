def sort_third_modified(l: list, m: list):
    concat_list = l + m
    sorted_list = []
    for i in range(len(concat_list)):
        if i % 3 == 0:
            sorted_list.append(concat_list[i])
    sorted_list.sort(reverse=True)
    result_list = []
    for i in range(len(concat_list)):
        if i % 3 == 0:
            result_list.append(sorted_list.pop(0))
        else:
            result_list.append(concat_list[i])
    return result_list