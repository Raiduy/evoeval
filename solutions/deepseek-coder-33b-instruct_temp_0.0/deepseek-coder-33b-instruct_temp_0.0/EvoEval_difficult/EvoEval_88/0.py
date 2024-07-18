def sort_array(array, pivot):
    if not array:
        return []
    pivot_value = array[pivot]
    before_pivot = [x for x in array[:pivot] if x < pivot_value]
    after_pivot = [x for x in array[pivot + 1:] if x >= pivot_value]
    pivot_list = [x for x in array[pivot:pivot + 1] if x == pivot_value]
    if (array[0] + pivot_value) % 2 == 0:
        before_pivot.sort(reverse=True)
    else:
        before_pivot.sort()
    after_pivot.sort()
    return before_pivot + pivot_list + after_pivot