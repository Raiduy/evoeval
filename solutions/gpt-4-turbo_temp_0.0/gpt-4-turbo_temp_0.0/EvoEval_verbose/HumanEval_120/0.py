
def maximum(arr, k):
    sorted_arr_desc = sorted(arr, reverse=True)
    max_k_elements = sorted_arr_desc[:k]
    return sorted(max_k_elements)