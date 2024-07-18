
def maximum(arr, k):
    """
    Given an array of integers 'arr' and a positive integer 'k', this function returns a sorted list of the top 'k' integers in 'arr'.
    """
    sorted_arr = sorted(arr, reverse=True)
    top_k_elements = sorted_arr[:k]
    return sorted(top_k_elements)