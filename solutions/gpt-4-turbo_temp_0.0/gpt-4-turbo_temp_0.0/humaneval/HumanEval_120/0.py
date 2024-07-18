
def maximum(arr, k):
    """
    Given an array arr of integers and a positive integer k, return a sorted list 
    of length k with the maximum k numbers in arr.
    """
    # Step 1: Sort the array in descending order
    sorted_arr = sorted(arr, reverse=True)
    
    # Step 2: Slice the first k elements
    max_k_elements = sorted_arr[:k]
    
    # Step 3: Return the sliced array sorted in ascending order
    return sorted(max_k_elements)
